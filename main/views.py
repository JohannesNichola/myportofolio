from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Johannes Nichola Simatupang",
        "npm": "2406495930",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "An Information Systems student at Universitas Indonesia with a strong interest in finance "
            "and business. Currently working as an IT Support and CRM Specialist at an fnb holding company. "
            "Love to learn new things every day (there is always room for growth)."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    experience_list = Experience.objects.all().order_by('-started_at')

    context = {
        "name": "Johannes Nichola Simatupang",
        "experience_list": experience_list,
    }
    return render(request, "experience.html", context)