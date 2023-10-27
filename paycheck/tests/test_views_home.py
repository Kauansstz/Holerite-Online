from django.test import TestCase as DjangoTestCasa
from django.urls import reverse
from unittest import TestCase


class PaycheckHomeTest(DjangoTestCasa):
    def test_view_home(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_view_home_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "pages/panel.html")
