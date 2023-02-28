from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def listar_posts(request):
    return render(request, 'listar_posts.html')

posts = [
    {
        "id": 1,
        "titulo": "post um"
    },

    {
        "id":2,
        "titulo": "post dois"
    },
]

def listar_posts(request):
    context = {
        "posts": posts 
    }
    return render(request, 'listar_posts.html', context)

def detalhe_post(request, id):
    post = posts[id-1]
    return render(request, 'detalhe_post.html', {"post": post})