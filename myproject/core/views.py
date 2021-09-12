import math

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

from .models import Person


def index(request):
    person_list = Person.objects.all()
    context = {'person_list': person_list}
    return render(request, 'index.html', context)
