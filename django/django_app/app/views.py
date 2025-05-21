from django.shortcuts import render
from .models import Post
# Create your views here.
def app_list(request):
    post = Post.objects.all()
    context = {
        'app_list' : post
    }
    return render(request, "app/app_list.html", context)