from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Movie

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def movie_details(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except ObjectDoesNotExist:
        return print("Movie not found.")
    return render(request, 'movie_details.html', {'movie': movie})


def home_page(request):
    user_name = request.GET.get('user_name')
    return render(request, 'home.html', {'user_name': user_name})