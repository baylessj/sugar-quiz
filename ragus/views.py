"""Defines the HTTP and JSON responses for the app's urls."""
import os

from django.contrib.auth import mixins
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import requests

from ragus.models import Door

AUTH_HEADERS = {"Authorization": f"Bearer {os.environ['AUTH_TOKEN']}"}


def index(request: HttpRequest) -> HttpResponse:
    """Get the landing page for the app."""
    if request.user.is_authenticated:
        return HttpResponseRedirect("home")
    return render(request, "index.html")


class Home(mixins.LoginRequiredMixin, generic.ListView):
    """Get the main page for logged in users. Allows access to doors."""

    model = Door

    def get_queryset(self) -> QuerySet:
        """Get the queryset for the view, including the current state of the doors."""
        doors = self.request.user.doors.all()
        for door in doors:
            response = requests.get(
                f"https://acme-locks-api.herokuapp.com/devices/{door.acme_device_id}/",
                headers=AUTH_HEADERS,
            )
            door.locked = response.json()["locked"]
        return doors


@csrf_exempt
@require_http_methods(["POST"])
def lock_door(request: HttpRequest, pk: str) -> JsonResponse:
    """Locks a Door, as long as it belongs to the requesting user.

    We hit this endpoint from the client instead of directly hitting the API endpoint to ensure
    that we do not leak the API Auth token.
    """
    # Check that we can actually unlock the given door
    if not request.user.doors.filter(acme_device_id=pk).exists():
        return JsonResponse({"error": "You are not authorized to lock this door."})

    # Hit the api, ignoring the response for now
    response = requests.get(
        f"https://acme-locks-api.herokuapp.com/devices/{pk}/lock", headers=AUTH_HEADERS
    )
    if not response.status_code == 200:
        return JsonResponse({"error": "Unable to unlock door."})

    return JsonResponse({})


@csrf_exempt
@require_http_methods(["POST"])
def unlock_door(request: HttpRequest, pk: str) -> JsonResponse:
    """Unlocks a Door, as long as it belongs to the requesting user.

    We hit this endpoint from the client instead of directly hitting the API endpoint to ensure
    that we do not leak the API Auth token.
    """
    # Check that we can actually unlock the given door
    if not request.user.doors.filter(acme_device_id=pk).exists():
        return JsonResponse({"error": "You are not authorized to unlock this door."})

    # Hit the api, ignoring the response for now
    response = requests.get(
        f"https://acme-locks-api.herokuapp.com/devices/{pk}/unlock",
        headers=AUTH_HEADERS,
    )
    if not response.status_code == 200:
        return JsonResponse({"error": "Unable to unlock door."})

    return JsonResponse({})
