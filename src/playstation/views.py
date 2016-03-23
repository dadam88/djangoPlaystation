from django.shortcuts import render

from .models import Game


# Create your views here.
def home_page(request):

    games = Game.objects.all()
    context = { 'message': 'Hello there',
                'games': games,
                
     }
    
    # Passes variables to home.html through context list of variables
    return render(request, "home.html", context)


def game_details(request, gameslug):

    game = Game.objects.get(slug=gameslug)
    
    context = { 'message': 'DETAILDETAIL PAGE',
                'game': game,
                
     }
    
    # Passes variables to home.html through context list of variables
    return render(request, "game_details.html", context)