# Generated by Django 4.2.9 on 2024-01-31 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_remove_map_file_map_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(upload_to='projects/thumbnails/'),
        ),
    ]
