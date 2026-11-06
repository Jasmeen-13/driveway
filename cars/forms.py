from datetime import date

from django import forms

from .models import Car


class CarForm(forms.ModelForm):
    """Create or edit a car without exposing its owner field."""

    class Meta:
        model = Car
        fields = [
            "make", "model", "price", "year", "mileage",
            "fuel_type", "transmission", "listing_url",
            "photo", "notes",
        ]
        labels = {
            "price": "Price (£)",
            "mileage": "Mileage (miles)",
            "listing_url": "Listing URL",
            "photo": "Car photo",
        }
        widgets = {
            "notes": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            css_class = (
                "form-select"
                if isinstance(field.widget, forms.Select)
                else "form-control"
            )
            field.widget.attrs["class"] = css_class

    def clean_year(self):
        year = self.cleaned_data["year"]
        if year > date.today().year + 1:
            raise forms.ValidationError(
                "Enter a year no later than next year."
            )
        return year

    def clean_photo(self):
        photo = self.cleaned_data.get("photo")
        if photo and hasattr(photo, "content_type"):
            if photo.size > 5 * 1024 * 1024:
                raise forms.ValidationError(
                    "Choose an image smaller than 5 MB."
                )
            if photo.content_type not in (
                "image/jpeg", "image/png", "image/webp"
            ):
                raise forms.ValidationError(
                    "Upload a JPG, PNG or WebP image."
                )
        return photo