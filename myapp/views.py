from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.
from django.views import View

from django.core import serializers
from .models import *


class Home(View):
    def get(self, request):
        contact = serializers.serialize('json', Contact.objects.all())
        interest = serializers.serialize('json', Interest.objects.all())
        skill = serializers.serialize('json', Skill.objects.all())
        project = serializers.serialize('json', Project.objects.all())
        print(contact)
        print(interest)
        print(skill)
        print(project)
        return JsonResponse({'contact': contact, 'interest': interest, 'skill': skill, 'project': project})

