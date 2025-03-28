"""Defines URL patterns for accounts."""

from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views

app_name = "accounts"
urlpatterns = [
    # Include default auth urls.
    path("", include("django.contrib.auth.urls")),
    # Registration page.
    path("register/", views.register, name="register"),
    # Logout
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
