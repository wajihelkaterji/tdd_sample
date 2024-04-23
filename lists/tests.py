from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page

class HomePage(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")