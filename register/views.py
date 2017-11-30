from django.contrib.auth.models import User
from django.shortcuts import render

from register.forms import RegisterForm


def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        data = form.cleaned_data
        email = data["email"]
        password = data["password"]
        confirm = data["confirmPassword"]

        if password == confirm:
            User.objects.create_user(email, email, password).save()

    return render(request, 'register/register.html', locals())
