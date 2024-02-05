from django.db import models
import uuid
from django.utils import timezone

class Label(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    date = models.DateField()
    labels = models.ManyToManyField(Label)
    thumbnail = models.ImageField(upload_to='projects/thumbnails/')
    sw_lat = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Southwest Latitude", default=53.299927)
    sw_lng = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Southwest Longitude", default = -6.240273)
    ne_lat = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Northeast Latitude", default = 53.313447)
    ne_lng = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Northeast Longitude", default = -6.205402)

    def __str__(self):
        return self.name

class Map(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, related_name='maps', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True, null=True)  # Optional description field
    gcs_url = models.URLField(blank=True, null=True)  # Optional Google Cloud Storage URL field
    
    # file = models.FileField(upload_to='maps/')

    def __str__(self):
        return f'{self.project.name} - {self.date}'