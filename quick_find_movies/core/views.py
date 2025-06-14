from django.shortcuts import render
# from django.http import HttpResponse
# import json
from .models import Movie

# Create your views here.
def movie_list(request):
    genre = request.GET.get("genre")
    year = request.GET.get("year")
    country = request.GET.get("country")

    movies = Movie.objects.all()

    if genre and genre !="all":
        movies = movies.filter(genre=genre)
    if year and year !="all":
        movies = movies.filter(year=year)
    if country and country !="all":
        movies = movies.filter(country=country)

    genres = Movie.objects.values_list("genre", flat=True).distinct()
    years = Movie.objects.values_list("year", flat=True).distinct().order_by("year")
    countries = Movie.objects.values_list("country", flat=True).distinct()

    context = {
        'movies': movies,
        'genres': genres,
        'years': years,
        'countries': countries,
        'selected_genre': genre,
        'selected_year': year,
        'selected_country': country,
    }
    # context_str = json.dumps(context, default=str)
    # return HttpResponse(context_str, content_type='application/json')
    return render(request, 'core/movie_list.html', context)