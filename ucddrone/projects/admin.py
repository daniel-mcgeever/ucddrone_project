from django.contrib import admin
from .models import Project, Map, Label

# Register your models here.
admin.site.register(Project)
admin.site.register(Map)
admin.site.register(Label)
