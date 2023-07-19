from django import forms

from blog.models import Blog


class BlogCreateForm(forms.ModelForm):

    class Meta:
        model = Blog
        exclude = ('view', 'date', 'author')

