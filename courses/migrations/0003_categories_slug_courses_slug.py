# Generated by Django 4.2.4 on 2023-10-03 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=models.CharField(default='selam', max_length=50),
        ),
        migrations.AddField(
            model_name='courses',
            name='slug',
            field=models.CharField(default='selam', max_length=50),
        ),
    ]
