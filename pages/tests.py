"""test.py"""

from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):
    """Test HomePageView url."""

    def test_url_exists_at_correct_location(self):
        """Test corect location at /"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """Test url reverse home"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """Test correct template name"""
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "pages/home.html")

    def test_template_content(self):
        """Test template home contain spesific html code"""
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Homepage</h1>")


class AboutpageTests(SimpleTestCase):
    """Test AboutPageView url."""

    def test_url_exists_at_correct_location(self):
        """Test corect location /about/"""
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """Test url reverse about"""
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """Test correct template name"""
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "pages/about.html")

    def test_template_content(self):
        """Test template about contain spesific html code"""
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About page</h1>")
