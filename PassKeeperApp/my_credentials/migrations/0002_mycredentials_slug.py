# Generated by Django 4.2.3 on 2023-08-01 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_credentials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycredentials',
            name='slug',
            field=models.SlugField(blank=True, default='', editable=False, max_length=255, unique=True),
        ),
    ]
