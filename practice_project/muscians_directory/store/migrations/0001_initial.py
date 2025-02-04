# Generated by Django 5.1.4 on 2025-01-30 02:09

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='muscian_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=11)),
                ('instrument_type', models.CharField(choices=[('guitar', 'Guitar'), ('flute', 'Flute'), ('drum', 'Drum')], default=None, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='album_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=20)),
                ('realse_date', models.DateField(default=django.utils.timezone.now)),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=0, max_length=20)),
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.muscian_model')),
            ],
        ),
    ]
