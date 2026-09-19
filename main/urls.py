from django.urls import path

from main.views import (
    show_main,
    show_experience,
    create_experience,
    edit_experience,
    get_experiences_json,
    delete_experience,
    show_education,
    show_project,
    create_project,
    edit_project,
    add_project_image,
    delete_project_image,
    get_projects_json,
    delete_project,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/create/", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/edit/", edit_experience, name="edit_experience"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("education/", show_education, name="show_education"),
    path("project/", show_project, name="show_project"),
    path("project/create/", create_project, name="create_project"),
    path("project/<uuid:project_id>/edit/", edit_project, name="edit_project"),
    path("project/<uuid:project_id>/add-image/", add_project_image, name="add_project_image"),
    path("project/<uuid:project_id>/delete-image/<uuid:image_id>/", delete_project_image, name="delete_project_image"),
    path("project/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("api/experiences/", get_experiences_json, name="get_experiences_json"),
]