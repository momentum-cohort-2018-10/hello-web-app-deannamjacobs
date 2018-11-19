from django.contrib import admin
from django.urls import path, include 
from django.views.generic import TemplateView #RedirectView
from collection import views
from collection.backends import MyRegistrationView
from django.contrib.auth.views import ( 
	PasswordResetView, PasswordResetDoneView, 
	PasswordResetConfirmView, PasswordResetCompleteView, 
)

urlpatterns = [
    path('', views.index, name='home'),
    path('about/',
        TemplateView.as_view(template_name='about.html'),
        name='about'),
    path('contact/',
        TemplateView.as_view(template_name='contact.html'),
        name='contact'),
    # path('blogs/', RedirectView.as_view(pattern_name='browse', permanent=True)),
    path('blogs/<slug>/', views.blog_detail,
        name='blog_detail'),
    path('blogs/<slug>/edit/',
        views.edit_blog, name='edit_blog'),
    # path('browse/', RedirectView.as_view(pattern_name='browse', permanent=True)),
    # path('browse/name/',
    #     views.browse_by_name, name='browse'),
    # path('browse/name/<initial>/',
    #     views.browse_by_name, name='browse_by_name'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/password/reset/', 
        PasswordResetView.as_view(template_name='registration/password_reset_form.html'), 
        name="password_reset"),
    path('accounts/password/reset/done/', 
        PasswordResetView.as_view(template_name='registration/password_reset_done.html'), 
        name="password_reset_done"),
    path('accounts/password/reset/<uidb64>/<token>/', 
        PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), 
        name="password_reset_confirm"),
    path('accounts/password/done/', 
        PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name="password_reset_complete"),
    path('accounts/register/', 
         MyRegistrationView.as_view(), name='registration_register'),
     path('accounts/create_blog/', 
         views.create_blog, name='registration_create_blog'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
]





