# Generated by Django 4.2.2 on 2023-07-04 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0006_recipes_text_fourth_recipes_text_second_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='food_type',
            field=models.CharField(default='', max_length=20),
        ),
    ]
