from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from sugar.views import index

urlpatterns = [
   path("", index, name="index"),
   path(
        "accounts/login/",
        auth_views.LoginView.as_view(redirect_authenticated_user=True),
        name="login",
    ),
    path("accounts/", include("django.contrib.auth.urls")),
   #  path("accounts/register/", register, name="register"),
]