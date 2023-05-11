from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'homepage/home.html', context)

def about(request):
    return render(request, 'homepage/about.html', {'title': 'About'})

