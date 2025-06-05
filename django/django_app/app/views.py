from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Movie
from rest_framework import generics
from .serializers import MovieSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

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

class MovieListCreate(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieByQuery(APIView):
    def get(self, request):
        movie_id = request.query_params.get('id')
        if not movie_id:
            return Response({"error": "Missing id query parameter"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            movie = Movie.objects.get(id=movie_id)
            serializer = MovieSerializer(movie)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
