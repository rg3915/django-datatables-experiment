import math

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

from .models import Person


def index(request):
    context = {}
    person_list = Person.objects.all()
    context['person_list'] = person_list
    return render(request, 'index.html', context)


def person_json(request):
    persons = Person.objects.all()
    total = persons.count()

    search = request.GET.get('search[value]')

    if search:
        persons = persons.filter(
            Q(name__icontains=search) |
            Q(email__icontains=search) |
            Q(phone__icontains=search)
        )

    _start = request.GET.get('start')
    _length = request.GET.get('length')
    if _start and _length:
        start = int(_start)
        length = int(_length)
        page = math.ceil(start / length) + 1  # [opcional]
        per_page = length  # [opcional]

        persons = persons[start:start + length]

    data = [person.to_dict_json() for person in persons]
    response = {
        'data': data,
        # 'page': page,  # [opcional]
        # 'per_page': per_page,  # [opcional]
        'recordsTotal': total,
        'recordsFiltered': total,
    }
    return JsonResponse(response)


def persons_serverside(request):
    template_name = 'persons_serverside.html'
    return render(request, template_name)
