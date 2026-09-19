from datetime import date

from django.test import TestCase
from django.urls import reverse

from main.models import Experience, Education, Project, ProjectImage, Skill

class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
        title="Asisten Dosen PBP",
        company="Universitas Indonesia",
        description="Membantu mahasiswa memahami pengembangan web.",
        category="part-time",
        started_at=date(2026, 1, 1),
        ended_at=None,
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(
            response,
            f'href="{reverse("main:show_experience")}"'
        )

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.company, "Universitas Indonesia")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")

        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.company)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Currently Working")

        self.assertContains(
            response,
            f'href="{reverse("main:show_main")}"'
        )

    def test_empty_experience_page(self):
        Experience.objects.all().delete()

        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "No experience has been added yet."
        )

    def test_completed_experience(self):
        self.experience.ended_at = date(2026, 8, 1)
        
        self.experience.save()

        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "No Longer Working")
        self.assertNotContains(response, "Currently Working")

class MainPageTest(TestCase):
    def setUp(self):
        self.skill = Skill.objects.create(
            title="Public Speaking",
            category="soft",
            description="Able to communicate ideas clearly and confidently.",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_main_page_contains_skill(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertContains(response, self.skill.title)
        self.assertContains(response, "Soft Skill")
        self.assertContains(response, self.skill.description)

    def test_main_page_navigation_links(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertContains(response, f'href="{reverse("main:show_education")}"')
        self.assertContains(response, f'href="{reverse("main:show_project")}"')

    def test_empty_skill_section(self):
        Skill.objects.all().delete()

        response = self.client.get(reverse("main:show_main"))

        self.assertContains(response, "No skill has been added yet.")

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)


class ExperienceTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            company="Universitas Indonesia",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
            started_at=date(2026, 1, 1),
            ended_at=None,
        )

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.company, "Universitas Indonesia")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")

        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.company)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Currently Working")

        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()

        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No experience has been added yet.")

    def test_completed_experience(self):
        self.experience.ended_at = date(2026, 8, 1)
        self.experience.save()

        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "No Longer Working")
        self.assertNotContains(response, "Currently Working")

class ExperienceCRUDTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            company="Universitas Indonesia",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
            started_at=date(2026, 1, 1),
            ended_at=None,
        )

    def test_create_experience_get(self):
        response = self.client.get(reverse("main:create_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience_form.html")
        self.assertContains(response, "Add New Experience")

    def test_create_experience_post_valid(self):
        response = self.client.post(reverse("main:create_experience"), {
            "title": "Backend Developer Intern",
            "company": "PT Contoh Sejahtera",
            "description": "Membangun REST API menggunakan Django.",
            "category": "internship",
            "started_at": "2026-01-01",
        })

        self.assertEqual(
            Experience.objects.filter(title="Backend Developer Intern").count(), 1
        )
        self.assertRedirects(response, reverse("main:show_experience"))

    def test_create_experience_post_invalid(self):
        response = self.client.post(reverse("main:create_experience"), {
            "title": "",
            "company": "PT Contoh Sejahtera",
            "description": "Tidak ada judul.",
            "category": "internship",
            "started_at": "2026-01-01",
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Experience.objects.count(), 1)

    def test_edit_experience_get(self):
        response = self.client.get(
            reverse("main:edit_experience", args=[self.experience.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience_form.html")
        self.assertContains(response, f"Edit {self.experience.title}")
        self.assertContains(response, self.experience.title)

    def test_edit_experience_post_valid(self):
        response = self.client.post(
            reverse("main:edit_experience", args=[self.experience.id]),
            {
                "title": "Asisten Dosen PBP Updated",
                "company": self.experience.company,
                "description": self.experience.description,
                "category": self.experience.category,
                "started_at": self.experience.started_at,
            }
        )

        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Asisten Dosen PBP Updated")
        self.assertRedirects(response, reverse("main:show_experience"))

    def test_edit_experience_post_invalid(self):
        response = self.client.post(
            reverse("main:edit_experience", args=[self.experience.id]),
            {
                "title": "",
                "company": self.experience.company,
                "description": self.experience.description,
                "category": self.experience.category,
                "started_at": self.experience.started_at,
            }
        )

        self.assertEqual(response.status_code, 200)
        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Asisten Dosen PBP")

    def test_edit_experience_not_found(self):
        response = self.client.get(
            reverse("main:edit_experience", args=["00000000-0000-0000-0000-000000000000"])
        )

        self.assertEqual(response.status_code, 404)

    def test_delete_experience_post(self):
        response = self.client.post(
            reverse("main:delete_experience", args=[self.experience.id])
        )

        self.assertRedirects(response, reverse("main:show_experience"))
        self.assertEqual(Experience.objects.filter(pk=self.experience.id).count(), 0)

    def test_delete_experience_get_does_not_delete(self):
        response = self.client.get(
            reverse("main:delete_experience", args=[self.experience.id])
        )

        self.assertRedirects(response, reverse("main:show_experience"))
        self.assertEqual(Experience.objects.filter(pk=self.experience.id).count(), 1)

    def test_get_experiences_json(self):
        response = self.client.get(reverse("main:get_experiences_json"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertContains(response, self.experience.title)

    def test_get_experiences_json_with_search(self):
        Experience.objects.create(
            title="Lain Sama Sekali",
            company="PT Lain",
            description="Deskripsi lain.",
            category="freelance",
            started_at=date(2026, 1, 1),
        )

        response = self.client.get(
            reverse("main:get_experiences_json"), {"title": "Asisten"}
        )

        self.assertContains(response, "Asisten Dosen PBP")
        self.assertNotContains(response, "Lain Sama Sekali")

    def test_search_experience_page(self):
        Experience.objects.create(
            title="Frontend Developer",
            company="PT Lain",
            description="Membangun UI menggunakan React.",
            category="freelance",
            started_at=date(2026, 1, 1),
        )

        response = self.client.get(
            reverse("main:show_experience"), {"title": "Asisten"}
        )

        self.assertContains(response, "Asisten Dosen PBP")
        self.assertNotContains(response, "Frontend Developer")

    def test_search_experience_no_result(self):
        response = self.client.get(
            reverse("main:show_experience"), {"title": "Tidak Ada"}
        )

        self.assertContains(response, "There is no experience with that title.")

class EducationTest(TestCase):
    def setUp(self):
        self.education = Education.objects.create(
            title="S1 Sistem Informasi",
            institution="Universitas Indonesia",
            description="Program studi Sistem Informasi, Fakultas Ilmu Komputer.",
            category="formal-edu",
            started_at=date(2024, 8, 1),
            ended_at=None,
        )

    def test_education_model(self):
        self.assertEqual(str(self.education), "S1 Sistem Informasi")
        self.assertEqual(self.education.institution, "Universitas Indonesia")
        self.assertEqual(self.education.category, "formal-edu")
        self.assertTrue(self.education.is_ongoing)

    def test_education_page(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")

        self.assertContains(response, self.education.title)
        self.assertContains(response, self.education.institution)
        self.assertContains(response, self.education.description)
        self.assertContains(response, "Formal-Edu")
        self.assertContains(response, "Currently Studying")

        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_education_page(self):
        Education.objects.all().delete()

        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No education has been added yet.")

    def test_completed_education(self):
        self.education.ended_at = date(2028, 6, 1)
        self.education.save()

        response = self.client.get(reverse("main:show_education"))

        self.assertFalse(self.education.is_ongoing)
        self.assertContains(response, "No Longer Studying")
        self.assertNotContains(response, "Currently Studying")


class ProjectTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="Website Portofolio",
            description="Website portofolio pribadi menggunakan Django.",
            category="academic",
            started_at=date(2026, 1, 1),
            ended_at=None,
        )

    def test_project_model(self):
        self.assertEqual(str(self.project), "Website Portofolio")
        self.assertEqual(self.project.category, "academic")
        self.assertTrue(self.project.is_ongoing)

    def test_project_page(self):
        response = self.client.get(reverse("main:show_project"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project.html")

        self.assertContains(response, self.project.title)
        self.assertContains(response, self.project.description)
        self.assertContains(response, "Academic")

        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_project_page(self):
        Project.objects.all().delete()

        response = self.client.get(reverse("main:show_project"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No project has been added yet.")


class SkillModelTest(TestCase):
    def test_skill_model(self):
        skill = Skill.objects.create(
            title="Basic Programming",
            category="technical",
            description="Basic understanding of Python, Java, HTML, CSS.",
        )

        self.assertEqual(str(skill), "Basic Programming")
        self.assertEqual(skill.category, "technical")
        self.assertEqual(skill.get_category_display(), "Technical Skill")

class ProjectCRUDTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="Website Portofolio",
            description="Website portofolio pribadi menggunakan Django.",
            category="academic",
            started_at=date(2026, 1, 1),
            ended_at=None,
        )

    def test_create_project_get(self):
        response = self.client.get(reverse("main:create_project"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project_form.html")
        self.assertContains(response, "Add New Project")

    def test_create_project_post_valid(self):
        response = self.client.post(reverse("main:create_project"), {
            "title": "Project Baru",
            "description": "Deskripsi project baru.",
            "category": "personal",
            "started_at": "2026-01-01",
        })

        self.assertEqual(Project.objects.filter(title="Project Baru").count(), 1)

        new_project = Project.objects.get(title="Project Baru")
        self.assertRedirects(
            response,
            reverse("main:add_project_image", args=[new_project.id])
        )

    def test_create_project_post_invalid(self):
        response = self.client.post(reverse("main:create_project"), {
            "title": "",
            "description": "Tidak ada judul.",
            "category": "personal",
            "started_at": "2026-01-01",
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Project.objects.count(), 1)

    def test_edit_project_get(self):
        response = self.client.get(reverse("main:edit_project", args=[self.project.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project_form.html")
        self.assertContains(response, f"Edit {self.project.title}")
        self.assertContains(response, self.project.title)

    def test_edit_project_post_valid(self):
        response = self.client.post(
            reverse("main:edit_project", args=[self.project.id]),
            {
                "title": "Website Portofolio Updated",
                "description": self.project.description,
                "category": self.project.category,
                "started_at": self.project.started_at,
            }
        )

        self.project.refresh_from_db()
        self.assertEqual(self.project.title, "Website Portofolio Updated")
        self.assertRedirects(response, reverse("main:show_project"))

    def test_edit_project_post_invalid(self):
        response = self.client.post(
            reverse("main:edit_project", args=[self.project.id]),
            {
                "title": "",
                "description": self.project.description,
                "category": self.project.category,
                "started_at": self.project.started_at,
            }
        )

        self.assertEqual(response.status_code, 200)
        self.project.refresh_from_db()
        self.assertEqual(self.project.title, "Website Portofolio")

    def test_edit_project_not_found(self):
        response = self.client.get(
            reverse("main:edit_project", args=["00000000-0000-0000-0000-000000000000"])
        )

        self.assertEqual(response.status_code, 404)

    def test_delete_project_post(self):
        response = self.client.post(reverse("main:delete_project", args=[self.project.id]))

        self.assertRedirects(response, reverse("main:show_project"))
        self.assertEqual(Project.objects.filter(pk=self.project.id).count(), 0)

    def test_delete_project_get_does_not_delete(self):
        response = self.client.get(reverse("main:delete_project", args=[self.project.id]))

        self.assertRedirects(response, reverse("main:show_project"))
        self.assertEqual(Project.objects.filter(pk=self.project.id).count(), 1)

    def test_get_projects_json(self):
        response = self.client.get(reverse("main:get_projects_json"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertContains(response, self.project.title)

    def test_get_projects_json_with_search(self):
        Project.objects.create(
            title="Lain Sama Sekali",
            description="Deskripsi lain.",
            category="personal",
            started_at=date(2026, 1, 1),
        )

        response = self.client.get(reverse("main:get_projects_json"), {"title": "Portofolio"})

        self.assertContains(response, "Website Portofolio")
        self.assertNotContains(response, "Lain Sama Sekali")


class ProjectImageTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="Website Portofolio",
            description="Website portofolio pribadi menggunakan Django.",
            category="academic",
            started_at=date(2026, 1, 1),
            ended_at=None,
        )

    def test_project_image_model(self):
        image = ProjectImage.objects.create(
            project=self.project,
            image="https://example.com/image.jpg",
            order=1,
        )

        self.assertEqual(str(image), f"{self.project.title} - Image 1")

    def test_add_project_image_get(self):
        response = self.client.get(
            reverse("main:add_project_image", args=[self.project.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project_image_form.html")
        self.assertContains(response, "5 image slots remaining.")

    def test_add_project_image_post_valid(self):
        response = self.client.post(
            reverse("main:add_project_image", args=[self.project.id]),
            {
                "image": "https://example.com/image.jpg",
                "order": 1,
            }
        )

        self.assertEqual(self.project.images.count(), 1)
        self.assertRedirects(
            response,
            reverse("main:add_project_image", args=[self.project.id])
        )

    def test_add_project_image_post_invalid(self):
        response = self.client.post(
            reverse("main:add_project_image", args=[self.project.id]),
            {
                "image": "",
                "order": 1,
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.project.images.count(), 0)

    def test_add_project_image_slot_full(self):
        for i in range(1, 6):
            ProjectImage.objects.create(
                project=self.project,
                image=f"https://example.com/image{i}.jpg",
                order=i,
            )

        response = self.client.get(
            reverse("main:add_project_image", args=[self.project.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "0 image slots remaining.")
        self.assertEqual(self.project.images.count(), 5)

    def test_delete_project_image(self):
        image = ProjectImage.objects.create(
            project=self.project,
            image="https://example.com/image.jpg",
            order=1,
        )

        response = self.client.post(
            reverse("main:delete_project_image", args=[self.project.id, image.id])
        )

        self.assertRedirects(
            response,
            reverse("main:add_project_image", args=[self.project.id])
        )
        self.assertEqual(self.project.images.count(), 0)

    def test_delete_project_image_not_found(self):
        response = self.client.post(
            reverse(
                "main:delete_project_image",
                args=[self.project.id, "00000000-0000-0000-0000-000000000000"]
            )
        )

        self.assertEqual(response.status_code, 404)

    def test_project_image_order_choices_exclude_used(self):
        ProjectImage.objects.create(
            project=self.project,
            image="https://example.com/image1.jpg",
            order=1,
        )
        ProjectImage.objects.create(
            project=self.project,
            image="https://example.com/image3.jpg",
            order=3,
        )

        response = self.client.get(
            reverse("main:add_project_image", args=[self.project.id])
        )

        form = response.context["form"]
        available = [choice[0] for choice in form.fields["order"].choices]

        self.assertNotIn(1, available)
        self.assertNotIn(3, available)
        self.assertIn(2, available)