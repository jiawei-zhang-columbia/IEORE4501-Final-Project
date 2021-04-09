import re
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

from .models import Sighting
from .forms import UpdateForm
from .forms import AddSightingForm


def index(request):

    def parse_date(date):
        date = str(date)

        return date

    sightings = Sighting.objects.all()
    for i in range(len(sightings)):
        sightings[i].date = parse_date(sightings[i].date)
    context = {
        'sightings': sightings
    }
    return render(request, 'squirrel_tracker/index.html', context)


def detail(request, unique_squirrel_id):
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        sighting = Sighting.objects.get(unique_squirrel_id=unique_squirrel_id)
        if form.is_valid():
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            shift = form.cleaned_data['shift']
            date = form.cleaned_data['date']
            age = form.cleaned_data['age']

            sighting.latitude = latitude
            sighting.longitude = longitude
            sighting.shift = shift
            sighting.date = date
            sighting.age = age

            sighting.save()
            messages.success(request, 'The sighting was successfully updated!')

        context = {
            'sighting': sighting,
            'form': form
        }

    else:
        sighting = get_object_or_404(Sighting, unique_squirrel_id=unique_squirrel_id)
        latitude = sighting.latitude
        longitude = sighting.longitude
        shift = sighting.shift
        date = sighting.date
        age = sighting.age
        form = UpdateForm(
            initial={
                'latitude': latitude,
                'longitude': longitude,
                'shift': shift,
                'date': date,
                'age': age
            }
        )
        context = {
            'sighting': sighting,
            'form': form
        }
    return render(request, 'squirrel_tracker/detail.html', context)



def add_sighting(request):
    if request.method == 'POST':
        form = AddSightingForm(request.POST)
        if form.is_valid():
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            unique_squirrel_id = form.cleaned_data['unique_squirrel_id']
            shift = form.cleaned_data['shift']
            date = form.cleaned_data['date']
            age = form.cleaned_data['age']
            primary_fur_color = form.cleaned_data['primary_fur_color']
            location = form.cleaned_data['location']
            specific_location = form.cleaned_data['specific_location']
            running = form.cleaned_data['running']
            chasing = form.cleaned_data['chasing']
            eating = form.cleaned_data['eating']
            foraging = form.cleaned_data['foraging']
            other_activities = form.cleaned_data['other_activities']
            kuks = form.cleaned_data['kuks']
            quaas = form.cleaned_data['quaas']
            moans = form.cleaned_data['moans']
            tail_flags = form.cleaned_data['tail_flags']
            tail_twitches = form.cleaned_data['tail_twitches']
            approaches = form.cleaned_data['approaches']
            indifferent = form.cleaned_data['indifferent']
            runs_from = form.cleaned_data['runs_from']
            climbing = form.cleaned_data['climbing']

            sighting = Sighting()
            sighting.unique_squirrel_id = unique_squirrel_id
            sighting.latitude = latitude
            sighting.longitude = longitude
            sighting.shift = shift
            sighting.date = date
            sighting.age = age
            sighting.primary_fur_color = primary_fur_color
            sighting.location = location
            sighting.specific_location = specific_location
            sighting.running = running
            sighting.chasing = chasing
            sighting.eating = eating
            sighting.foraging = foraging
            sighting.other_activities = other_activities
            sighting.kuks = kuks
            sighting.quaas = quaas
            sighting.moans = moans
            sighting.tail_flags = tail_flags
            sighting.tail_twitches = tail_twitches
            sighting.approaches = approaches
            sighting.indifferent = indifferent
            sighting.runs_from = runs_from
            sighting.climbing = climbing

            sighting.save()

            form = AddSightingForm()

            messages.success(request, 'A new sighting was successfully added!')

    else:
        form = AddSightingForm()

    return render(request, 'squirrel_tracker/add.html', {'form': form})

def show_map(request):
    sightings = Sighting.objects.all()[:100]
    context = {
        'sightings':sightings
    }
    return render(request,'squirrel_tracker/map.html',context)


def stats(request):
    num_of_sightings = Sighting.objects.all().count()
    num_of_squirrel = Sighting.objects.values("unique_squirrel_id").distinct().count()
    juvenile_age = Sighting.objects.filter(age='Juvenile').count()
    gray_fur = Sighting.objects.filter(primary_fur_color='Gray').count()
    ground_plane_location = Sighting.objects.filter(
        location='Ground Plane').count()
    running = Sighting.objects.filter(running='True').count()
    context = {
        'num_of_sightings': num_of_sightings,
        'num_of_squirrel': num_of_squirrel,
        'juvenile_age': juvenile_age,
        'gray_fur': gray_fur,
        'ground_plane_location': ground_plane_location,
        'running': running,
    }

    return render(request,'squirrel_tracker/stats.html',context)