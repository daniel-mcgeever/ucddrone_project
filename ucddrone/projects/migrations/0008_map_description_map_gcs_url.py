# Generated by Django 4.2.9 on 2024-02-03 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_project_ne_lat_project_ne_lng_project_sw_lat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='map',
            name='gcs_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
