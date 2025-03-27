from django.urls import path
from . import views

app_name = "pizzas"
urlpatterns = [
    # Page that shows all pizzas.
    path("", views.index, name="index"),
    # Page that shows pizza's details.
    path("<int:pizza_id>/", views.pizza_detail, name="pizza_detail"),
]
