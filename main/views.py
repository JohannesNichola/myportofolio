from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import ProjectForm, ProjectImageForm
from main.models import Experience, Education, Project, Skill


def show_main(request):
    skill_list = Skill.objects.all()

    context = {
        "name": "Johannes Nichola Simatupang",
        "npm": "2406495930",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "An Information Systems student at Universitas Indonesia with a strong interest in finance "
            "and business. Currently working as an IT Support and CRM Specialist at an fnb holding company. "
            "Love to learn new things every day (there is always room for growth)."
        ),
        "skill_list": skill_list,
    }
    return render(request, "index.html", context)


def show_experience(request):
    experience_list = Experience.objects.all().order_by('-started_at')

    context = {
        "name": "Johannes Nichola Simatupang",
        "experience_list": experience_list,
    }
    return render(request, "experience.html", context)

def show_education(request):
    education_list = Education.objects.all().order_by('-started_at')

    context = {
        "name": "Johannes Nichola Simatupang",
        "education_list": education_list,
    }
    return render(request, "education.html", context)

def show_project(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Johannes Nichola Simatupang",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)


def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_project")

    return redirect("main:show_project")

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        project = form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:add_project_image", project_id=project.id)

    context = {
        "name": "Johannes Nichola Simatupang",
        "form": form,
    }
    return render(request, "project_form.html", context)


def add_project_image(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    existing_images = project.images.count()

    if existing_images >= 5:
        messages.warning(request, "Project ini sudah mencapai batas maksimal 5 gambar.")
        return redirect("main:show_project")

    form = ProjectImageForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        image = form.save(commit=False)
        image.project = project
        image.save()
        messages.success(request, "Gambar berhasil ditambahkan!")
        return redirect("main:add_project_image", project_id=project.id)

    context = {
        "name": "Johannes Nichola Simatupang",
        "project": project,
        "form": form,
        "existing_images": project.images.all(),
        "remaining_slots": 5 - existing_images,
    }
    return render(request, "project_image_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")