from django.shortcuts import render

from models import Club


def show_home(request):
    clubs = Club.objects.all()
    return render(request, 'home/home.html', locals())


def show_club(request):
    # club = Club.objects.get(id=1)
    club=request.path
    return render(request, 'home/club.html', locals())
