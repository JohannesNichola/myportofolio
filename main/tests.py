from datetime import date

from django.test import TestCase
from django.urls import reverse

from main.models import Experience, Education, Project, Skill

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