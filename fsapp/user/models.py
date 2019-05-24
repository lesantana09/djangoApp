from django.contrib import admin
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    company = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
