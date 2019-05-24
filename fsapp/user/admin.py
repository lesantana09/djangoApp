from django.contrib import admin

from .models import User, UserModelAdmin

admin.site.register(User, UserModelAdmin)
