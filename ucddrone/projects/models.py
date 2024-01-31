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

    def __str__(self):
        return self.name

class Map(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, related_name='maps', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    # file = models.FileField(upload_to='maps/')

    def __str__(self):
        return f'{self.project.name} - Map'
