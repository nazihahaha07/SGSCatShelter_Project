# Generated by Django 4.2.4 on 2024-06-19 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catshelter', '0008_volunteerdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerdate',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='VolunteerApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('volunteer_date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catshelter.volunteerdate')),
            ],
        ),
    ]
