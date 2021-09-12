import string
from random import choice

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker

from myproject.core.models import Person

fake = Faker()


def gen_digits(max_length: int):
    '''Gera dígitos numéricos.'''
    return str(''.join(choice(string.digits) for i in range(max_length)))


def gen_first_name():
    return fake.first_name()


def gen_last_name():
    return fake.last_name()


def gen_email(first_name: str, last_name: str, company: str = None):
    first_name = slugify(first_name)
    last_name = slugify(last_name)
    email = f'{first_name}.{last_name}@email.com'
    return email


def gen_phone():
    return f'{gen_digits(2)} {gen_digits(4)}-{gen_digits(4)}'


def gen_status():
    return choice(('p', 'c', 'a'))


def create_person():
    aux_list = []
    Person.objects.all().delete()
    for _ in range(100):
        name = f'{fake.first_name()} {fake.last_name()}'
        email = f'{slugify(name)}@email.com'
        phone = gen_phone()
        status = gen_status()
        obj = Person(
            name=name,
            email=email,
            phone=phone,
            status=status,
        )
        aux_list.append(obj)

    Person.objects.bulk_create(aux_list)


class Command(BaseCommand):
    help = "Create person data."

    def handle(self, *args, **options):
        create_person()
