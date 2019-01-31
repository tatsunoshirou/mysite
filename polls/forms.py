from django import forms
from polls.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'title', 'message')
