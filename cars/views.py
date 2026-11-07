from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CarForm
from .models import Car


@login_required
def car_list(request):
    cars = Car.objects.filter(owner=request.user)
    return render(request, "cars/car_list.html", {"cars": cars})


@login_required
def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk, owner=request.user)
    return render(request, "cars/car_detail.html", {"car": car})


@login_required
def car_create(request):
    form = CarForm()

    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            messages.success(request, "Car added to your shortlist.")
            return redirect("cars:detail", pk=car.pk)

    return render(
        request,
        "cars/car_form.html",
        {"form": form, "page_title": "Add a car"},
    )


@login_required
def car_update(request, pk):
    car = get_object_or_404(Car, pk=pk, owner=request.user)
    form = CarForm(instance=car)

    if request.method == "POST":
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            messages.success(request, "Car details updated.")
            return redirect("cars:detail", pk=car.pk)

    return render(
        request,
        "cars/car_form.html",
        {"form": form, "page_title": "Edit car"},
    )


@login_required
def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk, owner=request.user)

    if request.method == "POST":
        car.delete()
        messages.success(request, "Car removed from your shortlist.")
        return redirect("cars:list")

    return render(
        request,
        "cars/car_confirm_delete.html",
        {"car": car},
    )
   
