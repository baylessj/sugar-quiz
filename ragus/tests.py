"""Unit tests for this app."""
import json

from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase

from ragus.models import User
from ragus.views import index, lock_door, unlock_door


class SimpleTest(TestCase):
    """Check that the landing page works when logged in."""

    def setUp(self) -> None:
        """Set up the necessary resources for the test."""
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_details(self) -> None:
        """Check that the landing page works when logged in."""
        # Create an instance of a GET request.
        request = self.factory.get("/")
        request.user = AnonymousUser()

        # Test not logged in
        response = index(request)
        self.assertEqual(response.status_code, 200)

        # Test logged in
        request = self.factory.get("/")
        request.user = User()
        response = index(request)
        self.assertEqual(response.status_code, 302)

class LockUnlockTest(TestCase):
    """Check good and bad requests to the lock and unlock methods"""
    def setUp(self) -> None:
        """Set up the necessary resources for the test."""
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_details(self) -> None:
        """Check bad requests to the lock and unlock methods"""
        # bad lock
        request = self.factory.post("/door/lock/abcdefg")
        request.user = User.objects.create_user("test@test.com", password="pass1234")

        response = lock_door(request, "abcdefg")
        self.assertEqual(json.loads(response.content)['error'], "You are not authorized to lock this door.")

        # Bad unlock
        request = self.factory.post("/door/unlock/abcdefg")
        request.user = User.objects.create_user("test1@test.com", password="pass1234")

        response = unlock_door(request, "abcdefg")
        self.assertEqual(json.loads(response.content)['error'], "You are not authorized to unlock this door.")

        # TODO: would need to mock requests to run the rest of the test.