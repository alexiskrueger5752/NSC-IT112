from django.urls import path
from .views import app_list
from .views import home_page

urlpatterns = [
    path("app_list/", app_list),
    path('', home_page, name='home')

]