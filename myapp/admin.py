from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Project, Contact, Interest, Skill)
class PersonAdmin(admin.ModelAdmin):
    pass