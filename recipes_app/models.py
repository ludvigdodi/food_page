from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Recipes(models.Model):
    name = models.CharField('Назва страв', max_length=30, blank=False)
    food_type = models.CharField('Тип їжі', max_length=20, blank=False, default='')
    short_desc = models.TextField('Короткий опис', max_length=80, blank=False)
    img = models.ImageField(null=True, blank=True, upload_to="media/", verbose_name='img')
    # text = models.TextField('text')
    text = RichTextUploadingField('Recipe')

    def __str__(self):
        return self.name


class Comments(models.Model):
    name = models.CharField("Ім'я", max_length=50)
    text_comments = models.TextField("Текст комментаря", max_length=2000)
    recipe = models.ForeignKey(Recipes, verbose_name='Post', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.text_comments}, {self.date_added}, {self.recipe}'


