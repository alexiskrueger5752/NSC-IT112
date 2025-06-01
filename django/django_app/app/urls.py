from django.urls import path
from .views import home_page, movie_list, movie_details

urlpatterns = [
    path('', home_page, name='home'),
    path("movies/", movie_list, name='movie_list'),
    path("movies/movie_details/<int:movie_id>", movie_details, name='movie_details'),
]
