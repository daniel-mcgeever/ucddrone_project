# Generated by Django 4.2.9 on 2024-02-03 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_remove_map_ne_lat_remove_map_ne_lng_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ne_lat',
            field=models.DecimalField(decimal_places=6, default=53.313447, max_digits=9, verbose_name='Northeast Latitude'),
        ),
        migrations.AddField(
            model_name='project',
            name='ne_lng',
            field=models.DecimalField(decimal_places=6, default=-6.205402, max_digits=9, verbose_name='Northeast Longitude'),
        ),
        migrations.AddField(
            model_name='project',
            name='sw_lat',
            field=models.DecimalField(decimal_places=6, default=53.299927, max_digits=9, verbose_name='Southwest Latitude'),
        ),
        migrations.AddField(
            model_name='project',
            name='sw_lng',
            field=models.DecimalField(decimal_places=6, default=-6.240273, max_digits=9, verbose_name='Southwest Longitude'),
        ),
    ]
