from django import forms
from .models import Project, Map

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'date', 'labels', 'thumbnail']

class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = ['date']
