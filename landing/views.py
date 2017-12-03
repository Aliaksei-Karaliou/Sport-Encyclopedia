from django.shortcuts import render

from landing.models import League


def landing(request):
    leagues = League.objects.all()
    return render(request, 'content/home.html', locals())


def leagues(request, league_id):
    league = League.objects.get(id=league_id)
    return render(request, 'content/league.html', locals())
