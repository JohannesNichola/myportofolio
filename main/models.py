import uuid
from django.db import models
from django.core.exceptions import ValidationError

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateField()
    ended_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None


class Education(models.Model):
    EDUCATION_CHOICES = [
        ('formal-edu', 'Formal-Edu'),
        ('certification', 'Certification'),
        ('course-bootcamp', 'Course-Bootcamp'),
        ('academic-project', 'Academic-project'),
        ('award-honor', 'Award-Honor'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=EDUCATION_CHOICES, default='formal-edu')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateField()
    ended_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None


class Project(models.Model):
    PROJECT_CATEGORIES = [
        ('academic', 'Academic'),
        ('professional', 'Professional'),
        ('personal', 'Personal'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=PROJECT_CATEGORIES, default='academic')
    started_at = models.DateField()
    ended_at = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.title

    @property
    def is_ongoing(self):
        return self.ended_at is None


class ProjectImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=1)

    def clean(self):
        if self.project_id:
            existing_images = ProjectImage.objects.filter(
                project=self.project
            ).exclude(pk=self.pk).count()

            if existing_images >= 5:
                raise ValidationError(
                    "Satu project maksimal memiliki 5 gambar."
                )

    def __str__(self):
        return f"{self.project.title} - Image {self.order}"