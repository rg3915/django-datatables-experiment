from django.urls import path
from myproject.core import views as v

app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
    path('persons/serverside/', v.persons_serverside, name='persons_serverside'),
    path('person/json/', v.person_json, name='person_json'),
]
