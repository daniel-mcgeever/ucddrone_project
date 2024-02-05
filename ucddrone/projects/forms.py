from django import forms
from .models import Project, Map

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'date', 'labels', 'thumbnail']

class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = ['date', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'}),  # Add the 'datepicker' class
        }

class ZipUploadForm(forms.Form):
    zip_file = forms.FileField(label='Select a zip file')

class MapUploadForm(forms.ModelForm):
    zip_file = forms.FileField()

    class Meta:
        model = Map
        fields = ['date', 'description']
        # widgets = {
        #     'date': forms.DateInput(attrs={'class': 'datepicker'}),  # Add the 'datepicker' class
        # }
    
        # , 'date', 'zip_file']
        # description = forms.CharField(max_length=255, required=False)
        # date = forms.DateField(required=True)
        # zip_file = forms.FileField()