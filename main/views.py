import datetime

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import ExperienceForm, EducationForm, ProjectForm, ProjectImageForm
from main.models import Experience, Education, Project, ProjectImage, Skill


def is_editor(user):
    return user.is_authenticated and user.groups.filter(name="Editor").exists()


def can_edit_portfolio_item(user):
    return user.is_superuser or is_editor(user)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Johannes Nichola Simatupang",
        "form": form,
    }
    return render(request, "register.html", context)


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Johannes Nichola Simatupang",
        "form": form,
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

def show_main(request):
    skill_list = Skill.objects.all()
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')

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
        "last_login": last_login,
    }
    return render(request, "index.html", context)


def show_experience(request):
    json_response = get_experiences_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Johannes Nichola Simatupang",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)


def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Johannes Nichola Simatupang",
        "form": form,
    }
    return render(request, "experience_form.html", context)


def edit_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience berhasil diupdate!")
        return redirect("main:show_experience")

    context = {
        "name": "Johannes Nichola Simatupang",
        "form": form,
        "experience": experience,
    }
    return render(request, "experience_form.html", context)


def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")


def get_experiences_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all().order_by("-started_at")

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")


def show_education(request):
    json_response = get_educations_json(request)

    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    educations = [education.object for education in educations]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Johannes Nichola Simatupang",
        "education_list": educations,
        "title_query": title_query,
    }
    return render(request, "education.html", context)


def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Education baru berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Johannes Nichola Simatupang",
        "form": form,
    }
    return render(request, "education_form.html", context)


def edit_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    form = EducationForm(request.POST or None, instance=education)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Education berhasil diupdate!")
        return redirect("main:show_education")

    context = {
        "name": "Johannes Nichola Simatupang",
        "form": form,
        "education": education,
    }
    return render(request, "education_form.html", context)


def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")


def get_educations_json(request):
    title_query = request.GET.get("title", "").strip()
    educations = Education.objects.all().order_by("-started_at")

    if title_query:
        educations = educations.filter(title__icontains=title_query)

    educations_json = serializers.serialize("json", educations)
    return HttpResponse(educations_json, content_type="application/json")

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
        "is_editor": is_editor(request.user),
    }
    return render(request, "project.html", context)


@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_project")

    return redirect("main:show_project")


@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied

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

@login_required(login_url="/login/")
def edit_project(request, project_id):
    if not can_edit_portfolio_item(request.user):
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project berhasil diupdate!")
        return redirect("main:show_project")

    context = {
        "name": "Johannes Nichola Simatupang",
        "form": form,
        "project": project,
    }
    return render(request, "project_form.html", context)


@login_required(login_url="/login/")
def add_project_image(request, project_id):
    if not can_edit_portfolio_item(request.user):
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)
    existing_images = project.images.count()

    if existing_images >= 5:
        messages.warning(request, "Project ini sudah mencapai batas maksimal 5 gambar.")

    form = ProjectImageForm(request.POST or None, project=project)

    if request.method == "POST" and existing_images < 5 and form.is_valid():
        image = form.save(commit=False)
        image.project = project
        image.save()
        messages.success(request, "Gambar berhasil ditambahkan!")
        return redirect("main:add_project_image", project_id=project.id)

    context = {
        "name": "Johannes Nichola Simatupang",
        "project": project,
        "form": form,
        "existing_images": project.images.all().order_by("order"),
        "remaining_slots": 5 - existing_images,
    }
    return render(request, "project_image_form.html", context)


@login_required(login_url="/login/")
def delete_project_image(request, project_id, image_id):
    if not can_edit_portfolio_item(request.user):
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)
    image = get_object_or_404(ProjectImage, pk=image_id, project=project)

    if request.method == "POST":
        image.delete()
        messages.success(request, "Gambar berhasil dihapus!")

    return redirect("main:add_project_image", project_id=project.id)


def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize(
        "json",
        projects,
        use_natural_foreign_keys=True,
        fields=("title", "description", "category", "started_at", "ended_at"),
    )
    return HttpResponse(projects_json, content_type="application/json")

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_project")