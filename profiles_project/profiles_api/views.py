from django.shortcuts import render
from profiles_api import models
from django.contrib import admin

admin.site.register(models.UserProfile)
