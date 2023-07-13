from django import forms
from .models import Comments, Recipes

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'text_comments')

