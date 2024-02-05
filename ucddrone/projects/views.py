import shutil, tempfile, uuid, mimetypes
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Project, Map
from .forms import ProjectForm, MapForm, MapUploadForm
import zipfile, os
from django.http import HttpResponse
from django.conf import settings
from google.cloud import storage

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

def project_map_list(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    maps = project.maps.all()
    return render(request, 'projects/project_map_list.html', {'project': project, 'maps': maps})

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'




def upload_map(request, project_id):

    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        form = MapUploadForm(request.POST, request.FILES)
        if form.is_valid():
            map_instance = form.save(commit=False)
            map_instance.project = project
            map_instance.save()
            

            map_id = map_instance.id
            # map = Map(project_id=project_id, description=description, date=date)


            # Get the uploaded zip file and other form data
            zip_file = form.cleaned_data['zip_file']
            description = form.cleaned_data['description']

            # Create a temporary directory to extract the zip contents
            temp_dir = tempfile.mkdtemp()

            try:
                # Extract the zip file to the temporary directory
                with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                    zip_ref.extractall(temp_dir)

                # Construct the dashless ids
                dashless_project_id = str(project_id).replace('-', '')
                dashless_map_id = str(map_id).replace('-', '')

                # Construct the GCS object path
                bucket_name = settings.GOOGLE_CLOUD_STORAGE_BUCKET_NAME
                project_folder = f'projects/{dashless_project_id}/maps'
                map_folder = dashless_map_id  # Use map ID as folder name
                map_path = f'{project_folder}/{map_folder}'

                # Initialize the GCS client
                storage_client = storage.Client()

                # Upload the extracted files to GCS while maintaining the folder structure
                for root, dirs, files in os.walk(temp_dir):
                    for file in files:

                        if file.startswith("._"):
                            continue

                        # Skip files with ".kml" extension
                        if file.endswith(".kml"):
                            continue

                        local_file_path = os.path.join(root, file)
                        relative_file_path_parts = os.path.relpath(local_file_path, temp_dir).split("/")
                        relative_file_path = "/".join(relative_file_path_parts[1:])
                        gcs_file_path = os.path.join(map_path, relative_file_path)

                        # print(f'root: {root}')
                        # print(f'local_file_path: {local_file_path}')
                        # print(f'relative_file_path_parts: {relative_file_path_parts}')

                        # print(f'relative_file_path: {relative_file_path}')
                        # print(f'gcs_file_path: {gcs_file_path}')
                        content_type, _ = mimetypes.guess_type(local_file_path)

                        # Upload the file to GCS
                        bucket = storage_client.bucket(bucket_name)
                        blob = bucket.blob(gcs_file_path)

                        blob.content_type = content_type

                        blob.upload_from_filename(local_file_path)

                # # Save the map record in the database (assuming you have a Map model)
                # map = Map(project_id=project_id, description=description, gcs_url=blob.public_url)
                # map.save()


                return redirect('project_map_list', project_id=project_id)
            finally:
                # Clean up the temporary directory
                shutil.rmtree(temp_dir)
        else:
            # Handle form validation errors
            pass
    else:
        form = MapUploadForm()
    return render(request, 'projects/upload_map.html', {'form': form})

