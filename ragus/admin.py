"""Register App Models for use in the admin interface here."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from ragus.models import Door, User

admin.site.register(User, UserAdmin)
admin.site.register(Door)
