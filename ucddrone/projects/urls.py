from django.urls import path
from .views import HomeView, create_project, add_maps, project_list, project_detail, project_map_list, upload_map

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create_project/', create_project, name='create_project'),
    path('add_maps/<uuid:project_id>/', add_maps, name='add_maps'),
    path('projects/', project_list, name='project_list'),
    path('projects/<uuid:project_id>/', project_detail, name='project_detail'),
    path('projects/<uuid:project_id>/maps/', project_map_list, name='project_map_list'),
    path('projects/<uuid:project_id>/upload_map', upload_map, name='upload_map'),
]