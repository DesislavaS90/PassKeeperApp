# Generated by Django 4.2.3 on 2023-07-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_alter_appuser_options_alter_appuser_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appuser',
            options={},
        ),
        migrations.AlterModelManagers(
            name='appuser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='appuser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='appuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='appuser',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='appuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
