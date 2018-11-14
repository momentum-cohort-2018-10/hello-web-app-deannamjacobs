from django.contrib import admin

from collection.models import Blog

class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}
    
admin.site.register(Blog, BlogAdmin)

# Register your models here.
