from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from landing.forms import SearchForm
from landing.models import League, Club, Player, PlayerHistory


def landing(request):
    leagues = League.objects.all().order_by('name')

    search = SearchForm(request.GET or None)

    if request.method == "GET" and search.is_valid():
        data = search.cleaned_data
        searched = data["search"]
        return HttpResponseRedirect('/search/' + searched)

    return render(request, 'content/home.html', locals())


def leagues(request, league_id):
    league = League.objects.get(id=league_id)
    title = league.name
    logo = league.logo
    clubs = Club.objects.filter(league=league_id).order_by('name')

    search = SearchForm(request.GET or None)

    if request.method == "GET" and search.is_valid():
        data = search.cleaned_data
        searched = data["search"]
        return HttpResponseRedirect('/search/' + searched)

    return render(request, 'content/league.html', locals())


def clubs(request, club_id):
    club = Club.objects.get(id=club_id)
    title = club.name
    logo = club.logo
    players = Player.objects.filter(club=club_id).order_by('shirt_number')

    search = SearchForm(request.GET or None)

    if request.method == "GET" and search.is_valid():
        data = search.cleaned_data
        searched = data["search"]
        return HttpResponseRedirect('/search/' + searched)

    return render(request, 'content/club.html', locals())


def players(request, player_id):
    player = Player.objects.get(id=player_id)
    title = player.full_name
    logo = player.photo
    history = PlayerHistory.objects.filter(player_id=player_id).order_by('start_year')

    search = SearchForm(request.GET or None)

    if request.method == "GET" and search.is_valid():
        data = search.cleaned_data
        searched = data["search"]
        return HttpResponseRedirect('/search/' + searched)

    return render(request, 'content/player.html', locals())


def search(request, data):
    leagues = League.objects.filter(name__contains=data).order_by('name')
    clubs = Club.objects.filter(name__contains=data).order_by('name')
    players = sorted(Player.objects.filter(
        Q(first_name__icontains=data) | Q(last_name__icontains=data) | Q(display_name__icontains=data)),
        key=lambda t: t.full_name)

    search = SearchForm(request.GET or None)
    search_data = data
    return render(request, 'content/search.html', locals())
