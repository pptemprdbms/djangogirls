from django.shortcuts import render
from trips.models import Post


def home(request):
    # get all posts
    post_list = Post.objects.all()
    return render(request,
                  'home.html',
                  {'post_list': post_list})


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post.html', {'post': post})