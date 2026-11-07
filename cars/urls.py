from django.urls import path

from . import views

app_name = "cars"

urlpatterns = [
    path("", views.car_list, name="list"),
    path("add/", views.car_create, name="create"),
    path("compare/", views.car_compare, name="compare"),
    path("<int:pk>/", views.car_detail, name="detail"),
    path("<int:pk>/edit/", views.car_update, name="update"),
    path("<int:pk>/delete/", views.car_delete, name="delete"),
]