from django.contrib import admin

from main.models import Experience, Education, Project, ProjectImage, Skill

admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(Skill)