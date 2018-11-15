from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from collection import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('blog/<slug>/', views.blog_detail, name='blog_detail'),
    path('blogs/<slug>/edit/',
        views.edit_blog, name='edit_blog'),
    path('admin/', admin.site.urls),
]
