from django.shortcuts import render

from models import Club


def home(request):
    clubs = Club.objects.all()
    return render(request, 'home/home.html', locals())
