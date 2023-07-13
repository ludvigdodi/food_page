from django import forms
from .models import Comments, Recipes
from django_ckeditor_5.widgets import CKEditor5Widget

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'text_comments')

