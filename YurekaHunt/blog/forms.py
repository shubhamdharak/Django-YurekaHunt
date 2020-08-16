from django import forms
from .models import Blog, contact
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title',
            'body',
            'image',
            'url',
            'hunter',
            'author',
            ]

class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'