from django.shortcuts import render
from collection.models import Blog

def index(request):
    blogs = Blog.objects.all()
    blog = "Blog name"
    return render(request, 'index.html', {'blogs': blogs,})

def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blogs/blog_detail.html', {'blog': blog,})