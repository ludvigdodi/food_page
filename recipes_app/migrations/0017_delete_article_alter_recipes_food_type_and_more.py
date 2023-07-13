# Generated by Django 4.2.3 on 2023-07-13 09:08

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0016_alter_recipes_text'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.AlterField(
            model_name='recipes',
            name='food_type',
            field=models.CharField(default='', max_length=20, verbose_name='Тип їжі'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Назва страв'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='short_desc',
            field=models.TextField(max_length=80, verbose_name='Короткий опис'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='text',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Recipe'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='text_second',
            field=models.TextField(default='-', verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='text_third',
            field=models.TextField(default='-', verbose_name='text'),
        ),
    ]
