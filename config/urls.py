from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from cars import account_views

urlpatterns = [
    path("", account_views.home, name="home"),
    path("admin/", admin.site.urls),
    path("cars/", include("cars.urls")),
    path("accounts/register/", account_views.register, name="register"),
    path(
        "accounts/login/",
        account_views.AccountLoginView.as_view(),
        name="login",
    ),
    path(
        "accounts/logout/",
        account_views.AccountLogoutView.as_view(),
        name="logout",
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
