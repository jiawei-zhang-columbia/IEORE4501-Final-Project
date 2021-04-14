from django.urls import path
from django.urls import re_path

from . import views

app_name = 'squirrel_tracker'

urlpatterns = [
    path('', views.new_index, name='index'),
    re_path(r'(?P<unique_squirrel_id>[0-9]+[A-Z]-[AP]M-[0-9]{4}-[0-9]{2})/$', views.detail, name='detail'),
    path('add/', views.add_sighting, name='add'),
    path('stats/', views.stats, name='stats'),
    path('sightings/', views.index, name='sightings'),
]
