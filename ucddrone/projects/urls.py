from django.urls import path
from .views import HomeView, create_project, add_maps, upload_zip, project_list, project_detail

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create_project/', create_project, name='create_project'),
    path('add_maps/<int:project_id>/', add_maps, name='add_maps'),
    path('upload_zip/', upload_zip, name='upload_zip'),
    path('projects/', project_list, name='project_list'),
    path('projects/<uuid:project_id>/', project_detail, name='project_detail'),
]