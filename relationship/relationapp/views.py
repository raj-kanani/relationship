from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from .models import Page, Post, Song


def home(request):
    return render(request, 'home.html')

def user(request):
    u = User.objects.all()
    return render(request, 'user.html', {'u': u})

def page(request):
    pa = Page.objects.all()
    return render(request, 'page.html', {'pa': pa})

def post(request):
    po = Post.objects.all()
    return render(request, 'post.html', {'po': po})

def song(request):
    # s = Song.objects.all()
    s = Song.objects.filter(user__username='avadh')
    return render(request, 'song.html', {'s': s})
