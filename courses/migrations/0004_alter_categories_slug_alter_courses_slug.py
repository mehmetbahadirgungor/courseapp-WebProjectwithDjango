# Generated by Django 4.2.4 on 2023-10-03 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_categories_slug_courses_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(default='selam'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='slug',
            field=models.SlugField(default='selam'),
        ),
    ]
