# Generated by Django 4.2.2 on 2023-07-03 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0005_alter_recipes_short_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='text_fourth',
            field=models.TextField(default='', verbose_name='text'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='text_second',
            field=models.TextField(default='', verbose_name='text'),
        ),
        migrations.AddField(
            model_name='recipes',
            name='text_third',
            field=models.TextField(default='', verbose_name='text'),
        ),
    ]