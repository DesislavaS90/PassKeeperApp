# Generated by Django 4.2.3 on 2023-08-07 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_credentials', '0002_mycredentials_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycredentials',
            name='password',
            field=models.BinaryField(),
        ),
    ]
