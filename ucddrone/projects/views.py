from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Project, Map
from .forms import ProjectForm, MapForm
import zipfile, os
from django.http import HttpResponse
from django.conf import settings

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            
            return redirect('add_maps', project_id=project.id)
    else:
        form = ProjectForm()
    return render(request, 'projects/create_project.html', {'form': form})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    maps = project.maps.all()

    return render(request, 'projects/project_detail.html', {'project': project, 'maps': maps})

def add_maps(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        form = MapForm(request.POST, request.FILES)
        if form.is_valid():
            map = form.save(commit=False)
            map.project = project
            map.save()
            # Redirect or inform of success
    else:
        form = MapForm()
    return render(request, 'projects/add_maps.html', {'form': form, 'project': project})

def upload_zip(request):
    if request.method == 'POST':
        zip_file = request.FILES.get('zip_file')
        if zip_file and zipfile.is_zipfile(zip_file):
            zip_path = os.path.join(settings.MEDIA_ROOT, zip_file.name)

            with open(zip_path, 'wb+') as destination:
                for chunk in zip_file.chunks():
                    destination.write(chunk)

            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(os.path.join(settings.MEDIA_ROOT, 'extracted'))

            os.remove(zip_path)  # Clean up the uploaded zip file
            return HttpResponse("Zip file uploaded and extracted successfully.")
        else:
            return HttpResponse("Invalid file format. Please upload a zip file.")

    return render(request, 'upload_zip.html')

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

# def home(request):
#     return render(request, 'projects/home.html')
