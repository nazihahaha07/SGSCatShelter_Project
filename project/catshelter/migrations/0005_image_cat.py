# Generated by Django 4.2.4 on 2024-06-12 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catshelter', '0004_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='catshelter.cat'),
        ),
    ]
