# Generated by Django 4.2.4 on 2024-06-08 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catshelter', '0002_cat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='image',
        ),
        migrations.RemoveField(
            model_name='cat',
            name='medical_history',
        ),
        migrations.AlterField(
            model_name='cat',
            name='age',
            field=models.IntegerField(),
        ),
    ]
