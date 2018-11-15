from django.forms import ModelForm
from collection.models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('name', 'description',)