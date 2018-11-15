from django.shortcuts import render, redirect
from collection.forms import BlogForm
from collection.models import Blog


def index(request):
    blogs = Blog.objects.all()
    blog = "Blog name"
    return render(request, 'index.html', {'blogs': blogs, })


def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blogs/blog_detail.html', {'blog': blog, })


def edit_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    form_class = BlogForm

    if request.method == 'POST':
        form = form_class(data=request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', slug=blog.slug)
    else:
        form = form_class(instance=blog)

    return render(request, 'blogs/edit_blog.html', {
        'blog': blog,
        'form': form,
    })
