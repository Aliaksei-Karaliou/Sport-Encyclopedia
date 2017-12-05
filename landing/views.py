from django.shortcuts import render

from landing.models import League, Club, Player, PlayerHistory


def landing(request):
    leagues = League.objects.all().order_by('name')
    return render(request, 'content/home.html', locals())


def leagues(request, league_id):
    league = League.objects.get(id=league_id)
    logo = league.logo
    clubs = Club.objects.filter(league=league_id).order_by('name')
    return render(request, 'content/league.html', locals())


def clubs(request, club_id):
    club = Club.objects.get(id=club_id)
    logo = club.logo
    players = Player.objects.filter(club=club_id).order_by('shirt_number')
    return render(request, 'content/club.html', locals())


def players(request, player_id):
    player = Player.objects.get(id=player_id)
    logo = player.photo
    history = PlayerHistory.objects.filter(player_id=player_id).order_by('start_year')
    return render(request, 'content/player.html', locals())
