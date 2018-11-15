from django.shortcuts import render
from collection.models import Blog

def index(request):
    blogs = Blog.objects.all()
    thing = "Thing name"
    return render(request, 'index.html', {'blogs': blogs,})