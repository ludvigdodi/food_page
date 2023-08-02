from django import forms
from .models import Comments, Recipes
from django.contrib.auth.models import User


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name','text_comments',)

