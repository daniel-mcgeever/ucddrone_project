from django.contrib import admin
from .models import Project, Map, Label
from guardian.admin import GuardedModelAdmin

class ProjectAdmin(GuardedModelAdmin):
    pass

# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Map)
admin.site.register(Label)
