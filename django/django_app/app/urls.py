from django.urls import path
from .views import home_page, movie_list, movie_details, MovieListCreate, MovieDetail, MovieByQuery

urlpatterns = [
    path('', home_page, name='home'),
    path("movies_page/", movie_list, name='movie_table'),
    path("movies/movie_details/<int:movie_id>", movie_details, name='movie_table_details'),
    path('movies/',  MovieListCreate.as_view(), name='movie_list'),
    path('movies/<int:pk>/', MovieDetail.as_view(), name='movie_details'),
    path('movies/query/', MovieByQuery.as_view(), name='movie_by_query'),
]
