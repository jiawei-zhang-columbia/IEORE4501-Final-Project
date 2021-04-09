from django.urls import path
from django.urls import re_path

from . import views

app_name = 'squirrel_tracker'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'(?P<unique_squirrel_id>[0-9]+[A-Z]-[AP]M-[0-9]{4}-[0-9]{2})/$', views.detail, name='detail'),
    # path('update_latitude/<unique_squirrel_id>', views.update_latitude, name='update_latitude'),
    # path('update_longitude/<unique_squirrel_id>', views.update_longitude, name='update_longitude'),
    # path('update_shift/<unique_squirrel_id>', views.update_shift, name='update_shift'),
    # path('update_date/<unique_squirrel_id>', views.update_date, name='update_date'),
    # path('update_age/<unique_squirrel_id>', views.update_age, name='update_age'),
    path('add/', views.add_sighting, name='add'),
    path('stats/', views.stats, name='stats'),
]

