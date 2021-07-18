"""Defines the exposed urls from this app."""
from django.contrib.auth import views as auth_views
from django.urls import include, path


from ragus.views import Home, index, lock_door, unlock_door

urlpatterns = [
    path("", index, name="index"),
    path("home", Home.as_view(), name="home"),
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(redirect_authenticated_user=True),
        name="login",
    ),
    path("accounts/", include("django.contrib.auth.urls")),
    path("doors/lock/<str:pk>/", lock_door, name="doors/lock"),
    path("doors/unlock/<str:pk>/", unlock_door, name="doors/unlock"),
]
