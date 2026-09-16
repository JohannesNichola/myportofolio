from django.forms import ModelForm, TextInput, Textarea, Select, DateInput

from main.models import Project, ProjectImage

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "category",
            "started_at",
            "ended_at",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "category": "Kategori Proyek",
            "started_at": "Tanggal Mulai",
            "ended_at": "Tanggal Selesai",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "category": Select(),
            "started_at": DateInput(
                attrs={
                    "type": "date",
                }
            ),
            "ended_at": DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }

class ProjectImageForm(ModelForm):
    class Meta:
        model = ProjectImage
        fields = ["image", "order"]
        labels = {
            "image": "URL Gambar",
            "order": "Urutan",
        }
        widgets = {
            "image": TextInput(
                attrs={"placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000"}
            ),
            "order": TextInput(attrs={"type": "number", "min": 1, "max": 5}),
        }