from __future__ import print_function

from django.shortcuts import render

from models import Sportsman


def home(request):
    sportsmen = Sportsman.objects.all()
    return render(request, 'home/home.html', locals())
