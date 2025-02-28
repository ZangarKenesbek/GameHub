from django.shortcuts import render, get_object_or_404
from .models import Game
from .utils import average_rating

def index(request):
    return render(request, "base.html")


def game_list(request):
    games = Game.objects.all()

    title_query = request.GET.get('title', '').strip()
    genre_query = request.GET.get('genre', '').strip()
    min_rating = request.GET.get('min_rating', '')

    if title_query:
        games = games.filter(title__icontains=title_query)

    if genre_query:
        games = games.filter(genre__icontains=genre_query)

    game_list = []
    for game in games:
        reviews = game.review_set.all()
        if reviews:
            game_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            game_rating = None
            number_of_reviews = 0

        if min_rating and game_rating is not None:
            if game_rating < float(min_rating):
                continue

        game_list.append({'game': game, 'game_rating': game_rating, 'number_of_reviews': number_of_reviews})

    context = {'game_list': game_list}
    return render(request, 'games/games_list.html', context)

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    reviews = game.review_set.all()
    game_rating = average_rating([review.rating for review in reviews]) if reviews else None
    return render(request, "games/game_detail.html", {"game": game, "game_rating": game_rating, "reviews": reviews})
