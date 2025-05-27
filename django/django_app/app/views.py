from django.shortcuts import render
from .models import Post
# Create your views here.
def app_list(request):
    post = Post.objects.all()
    context = {
        'app_list' : post
    }
    return render(request, "app_list.html", context)

def home_page(request):
    user_name = request.GET.get('user_name')
    return render(request, 'base.html', {'user_name': user_name})