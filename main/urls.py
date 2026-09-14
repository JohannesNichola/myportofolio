from django.urls import path

from main.views import show_main, show_experience, show_education, show_project, show_skill

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    path("project/", show_project, name="show_project"),
    path("skill/", show_skill, name="show_skill"),
]