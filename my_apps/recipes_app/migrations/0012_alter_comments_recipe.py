# Generated by Django 4.2.2 on 2023-07-10 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0011_alter_comments_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes_app.recipes', verbose_name='Post'),
        ),
    ]
