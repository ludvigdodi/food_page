# Generated by Django 4.2.2 on 2023-07-05 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0008_remove_recipes_text_fourth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='short_desc',
            field=models.TextField(max_length=80),
        ),
    ]
