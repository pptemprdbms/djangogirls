from django.shortcuts import render
from trips.models import Post


def home(request):
    # get all the posts
    post_list = Post.objects.all()
    return render(request,
                  'templates/home.html',
                  {'post_list': post_list})