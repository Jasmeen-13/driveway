from datetime import date
from urllib.parse import parse_qs, urlsplit

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .forms import CarForm
from .models import Car


def car_form_data(**overrides):
    data = {
        "make": "Test make",
        "model": "Test model",
        "price": "12000.00",
        "year": date.today().year,
        "mileage": 25000,
        "fuel_type": Car.FuelType.PETROL,
        "transmission": Car.Transmission.MANUAL,
        "listing_url": "",
        "notes": "",
    }
    data.update(overrides)
    return data


class CarViewsTests(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.owner = user_model.objects.create_user(
            username="owner",
            password="test-password",
        )
        self.other_user = user_model.objects.create_user(
            username="other",
            password="test-password",
        )
        self.owner_car = self.create_car(self.owner, "Owner car")
        self.second_owner_car = self.create_car(self.owner, "Second owner car")
        self.other_car = self.create_car(self.other_user, "Other user's car")
        self.client.force_login(self.owner)

    @staticmethod
    def create_car(owner, make):
        return Car.objects.create(
            owner=owner,
            make=make,
            model="Test model",
            price="12000.00",
            year=date.today().year,
            mileage=25000,
            fuel_type=Car.FuelType.PETROL,
            transmission=Car.Transmission.MANUAL,
        )

    def test_logged_out_users_are_redirected_to_login(self):
        self.client.logout()
        paths = [
            reverse("cars:list"),
            reverse("cars:create"),
            reverse("cars:compare"),
            reverse("cars:detail", args=[self.owner_car.pk]),
            reverse("cars:update", args=[self.owner_car.pk]),
            reverse("cars:delete", args=[self.owner_car.pk]),
        ]

        for path in paths:
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertEqual(response.status_code, 302)
                redirect = urlsplit(response.url)
                self.assertEqual(redirect.path, reverse("login"))
                self.assertEqual(
                    parse_qs(redirect.query).get("next"),
                    [path],
                )

    def test_shortlist_contains_only_the_logged_in_users_cars(self):
        shortlists = (
            (self.owner, {self.owner_car.pk, self.second_owner_car.pk}),
            (self.other_user, {self.other_car.pk}),
        )

        for user, expected_ids in shortlists:
            with self.subTest(user=user.username):
                self.client.force_login(user)
                response = self.client.get(reverse("cars:list"))

                self.assertEqual(response.status_code, 200)
                self.assertSetEqual(
                    set(
                        response.context["cars"].values_list(
                            "pk", flat=True
                        )
                    ),
                    expected_ids,
                )

    def test_owner_can_create_a_car_and_is_assigned_as_owner(self):
        response = self.client.post(
            reverse("cars:create"),
            car_form_data(make="New car"),
        )

        car = Car.objects.get(make="New car")
        self.assertRedirects(
            response,
            reverse("cars:detail", args=[car.pk]),
        )
        self.assertEqual(car.owner, self.owner)

    def test_owner_can_view_a_car(self):
        response = self.client.get(
            reverse("cars:detail", args=[self.owner_car.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["car"], self.owner_car)

    def test_owner_can_edit_a_car(self):
        response = self.client.post(
            reverse("cars:update", args=[self.owner_car.pk]),
            car_form_data(make="Updated make", price="15000.00"),
        )

        self.assertRedirects(
            response,
            reverse("cars:detail", args=[self.owner_car.pk]),
        )
        self.owner_car.refresh_from_db()
        self.assertEqual(self.owner_car.make, "Updated make")
        self.assertEqual(str(self.owner_car.price), "15000.00")

    def test_owner_can_delete_a_car(self):
        response = self.client.post(
            reverse("cars:delete", args=[self.owner_car.pk])
        )

        self.assertRedirects(response, reverse("cars:list"))
        self.assertFalse(Car.objects.filter(pk=self.owner_car.pk).exists())

    def test_get_on_delete_page_does_not_delete_the_car(self):
        response = self.client.get(
            reverse("cars:delete", args=[self.owner_car.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Car.objects.filter(pk=self.owner_car.pk).exists())

    def test_another_user_gets_404_for_detail_edit_and_delete_pages(self):
        self.client.force_login(self.other_user)
        paths = [
            reverse("cars:detail", args=[self.owner_car.pk]),
            reverse("cars:update", args=[self.owner_car.pk]),
            reverse("cars:delete", args=[self.owner_car.pk]),
        ]

        for path in paths:
            with self.subTest(path=path):
                self.assertEqual(self.client.get(path).status_code, 404)

    def test_another_users_post_requests_cannot_edit_or_delete_a_car(self):
        self.client.force_login(self.other_user)

        update_response = self.client.post(
            reverse("cars:update", args=[self.owner_car.pk]),
            car_form_data(make="Unauthorized edit", price="1.00"),
        )
        self.assertEqual(update_response.status_code, 404)

        self.owner_car.refresh_from_db()
        self.assertEqual(self.owner_car.make, "Owner car")
        self.assertEqual(str(self.owner_car.price), "12000.00")

        delete_response = self.client.post(
            reverse("cars:delete", args=[self.owner_car.pk])
        )
        self.assertEqual(delete_response.status_code, 404)
        self.assertTrue(Car.objects.filter(pk=self.owner_car.pk).exists())

    def test_comparison_accepts_two_or_three_owned_cars(self):
        third_owner_car = self.create_car(self.owner, "Third owner car")

        for cars in (
            [self.owner_car, self.second_owner_car],
            [self.owner_car, self.second_owner_car, third_owner_car],
        ):
            with self.subTest(car_count=len(cars)):
                response = self.client.get(
                    reverse("cars:compare"),
                    {"car": [car.pk for car in cars]},
                )

                self.assertEqual(response.status_code, 200)
                self.assertSetEqual(
                    {car.pk for car in response.context["cars"]},
                    {car.pk for car in cars},
                )

    def test_comparison_rejects_invalid_selections(self):
        third_owner_car = self.create_car(self.owner, "Third owner car")
        fourth_owner_car = self.create_car(self.owner, "Fourth owner car")
        invalid_selections = {
            "zero cars": [],
            "one car": [self.owner_car.pk],
            "four cars": [
                self.owner_car.pk,
                self.second_owner_car.pk,
                third_owner_car.pk,
                fourth_owner_car.pk,
            ],
            "invalid id": [self.owner_car.pk, "not-a-car-id"],
            "another user's car": [self.owner_car.pk, self.other_car.pk],
        }

        for description, selected_ids in invalid_selections.items():
            with self.subTest(selection=description):
                response = self.client.get(
                    reverse("cars:compare"),
                    {"car": selected_ids},
                )

                self.assertRedirects(response, reverse("cars:list"))


class CarFormTests(TestCase):
    def test_form_rejects_negative_price(self):
        form = CarForm(data=car_form_data(price="-1.00"))

        self.assertFalse(form.is_valid())
        self.assertIn("price", form.errors)

    def test_form_rejects_negative_mileage(self):
        form = CarForm(data=car_form_data(mileage="-1"))

        self.assertFalse(form.is_valid())
        self.assertIn("mileage", form.errors)

    def test_form_rejects_year_more_than_one_year_ahead(self):
        form = CarForm(data=car_form_data(year=date.today().year + 2))

        self.assertFalse(form.is_valid())
        self.assertIn("year", form.errors)
