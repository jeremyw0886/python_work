from django.shortcuts import render, redirect
from .forms import RegistrationForm


def register(request):
    """Register a new user."""
    if request.method != "POST":
        form = RegistrationForm()
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally log the user in automatically here.
            return redirect("accounts:login")
    context = {"form": form}
    return render(request, "accounts/register.html", context)
