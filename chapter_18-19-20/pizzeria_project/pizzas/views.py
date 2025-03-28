from django.shortcuts import render, get_object_or_404
from .models import Pizza


# Create your views here.
def index(request):
    """Show all availabel pizzas."""
    pizzas = Pizza.objects.all()
    context = {"pizzas": pizzas}
    return render(request, "pizzas/index.html", context)


def pizza_detail(request, pizza_id):
    """Show a single pizza and its toppings."""
    pizza = get_object_or_404(Pizza, id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {"pizza": pizza, "toppings": toppings}
    return render(request, "pizzas/pizza_detail.html", context)
