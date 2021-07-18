"""Unit tests for this app."""
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase

from ragus.views import index


class SimpleTest(TestCase):
    """An example test."""

    def setUp(self) -> None:
        """Set up the necessary resources for the test."""
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_details(self) -> None:
        """An example test."""
        # Create an instance of a GET request.
        request = self.factory.get("/")
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = index(request)
        self.assertEqual(response.status_code, 200)
