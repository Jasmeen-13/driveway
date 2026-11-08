from decimal import Decimal

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class Car(models.Model):
    """A car saved to a user's personal shortlist."""

    class FuelType(models.TextChoices):
        PETROL = "petrol", "Petrol"
        DIESEL = "diesel", "Diesel"
        HYBRID = "hybrid", "Hybrid"
        PETROL_PHEV = "petrol_phev", "Petrol plug-in hybrid"
        ELECTRIC = "electric", "Electric"
        OTHER = "other", "Other"

    class Transmission(models.TextChoices):
        MANUAL = "manual", "Manual"
        AUTOMATIC = "automatic", "Automatic"
        OTHER = "other", "Other"

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cars",
    )
    make = models.CharField(max_length=80)
    model = models.CharField(max_length=120)
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    year = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1886)],
    )
    mileage = models.PositiveIntegerField()
    fuel_type = models.CharField(
        max_length=20,
        choices=FuelType.choices,
    )
    transmission = models.CharField(
        max_length=20,
        choices=Transmission.choices,
    )
    listing_url = models.URLField(max_length=2000, blank=True)
    photo = models.ImageField(upload_to="cars/", blank=True)
    notes = models.TextField(max_length=2000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at", "-pk"]

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"