import os

from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.views import generic
from django.contrib.auth import mixins
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import requests

from ragus.models import Door

AUTH_HEADERS = {"Authorization": f"Bearer {os.environ['AUTH_TOKEN']}"}

def index(request):
   if request.user.is_authenticated:
      return HttpResponseRedirect("home")
   return render(request, 'index.html')

def home(request):
   return render(request, "home.html") 

class Home(mixins.LoginRequiredMixin, generic.ListView):
   model = Door

   def get_queryset(self):
      doors = self.request.user.doors.all()
      for door in doors:
         response = requests.get(f"https://acme-locks-api.herokuapp.com/devices/{door.acme_device_id}/", headers=AUTH_HEADERS)
         door.locked = response.json()["locked"]
      return doors

@csrf_exempt
@require_http_methods(["POST"])
def lock_door(request, pk):
   """Locks a Door, as long as it belongs to the requesting user.
   
   We hit this endpoint from the client instead of directly hitting the API endpoint to ensure
   that we do not leak the API Auth token.
   """
   # Check that we can actually unlock the given door
   if not request.user.doors.filter(acme_device_id=pk).exists():
      return JsonResponse({'error': 'You are not authorized to lock this door'})

   # Hit the api, ignoring the response for now
   # TODO: handle any error conditions from the API here
   response = requests.get(f"https://acme-locks-api.herokuapp.com/devices/{pk}/lock", headers=AUTH_HEADERS)

   return JsonResponse({})

@csrf_exempt
@require_http_methods(["POST"])
def unlock_door(request, pk):
   """Unlocks a Door, as long as it belongs to the requesting user.
   
   We hit this endpoint from the client instead of directly hitting the API endpoint to ensure
   that we do not leak the API Auth token.
   """
   # Check that we can actually unlock the given door
   if not request.user.doors.filter(acme_device_id=pk).exists():
      return JsonResponse({'error': 'You are not authorized to unlock this door'})

   # Hit the api, ignoring the response for now
   # TODO: handle any error conditions from the API here
   response = requests.get(f"https://acme-locks-api.herokuapp.com/devices/{pk}/unlock", headers=AUTH_HEADERS)

   return JsonResponse({})
