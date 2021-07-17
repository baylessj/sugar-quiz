from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ragus.models import User, Door

admin.site.register(User, UserAdmin)
admin.site.register(Door)