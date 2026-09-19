from django import forms
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
            "title": "Project Title",
            "description": "Project Description",
            "category": "Project Category",
            "started_at": "Start Date",
            "ended_at": "End Date",
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
                    "placeholder": "Tell me about your project",
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
    order = forms.ChoiceField(label="Order")

    class Meta:
        model = ProjectImage
        fields = ["image", "order"]
        labels = {
            "image": "Image URL",
        }
        widgets = {
            "image": TextInput(
                attrs={"placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000"}
            ),
        }

    def __init__(self, *args, project=None, **kwargs):
        super().__init__(*args, **kwargs)

        all_slots = set(range(1, 6))
        used_slots = set()

        if project is not None:
            used_slots = set(
                project.images.values_list("order", flat=True)
            )

        available_slots = sorted(all_slots - used_slots)

        self.fields["order"].choices = [
            (slot, f"Order-{slot}") for slot in available_slots
        ]

        if not available_slots:
            self.fields["order"].widget.attrs["disabled"] = True

    def clean_order(self):
        order = self.cleaned_data.get("order")
        return int(order)
