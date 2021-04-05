import re
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

from .models import Sighting
from .forms import LatitudeForm
from .forms import LongitudeForm
from .forms import ShiftForm
from .forms import DateForm
from .forms import AgeForm
from .forms import AddSightingForm


def index(request):

    def parse_date(date):
        date = str(date)
        # month = date[:2]
        # day = date[2:4]
        # year = date[4:]
        #
        # date = month + '-' + day + '-' + year

        return date

    sightings = Sighting.objects.all()
    for i in range(len(sightings)):
        sightings[i].date = parse_date(sightings[i].date)
    context = {
        'sightings': sightings
    }
    return render(request, 'squirrel_tracker/index.html', context)


def detail(request, unique_squirrel_id):
    sighting = get_object_or_404(Sighting, unique_squirrel_id=unique_squirrel_id)
    context = {
        'sighting': sighting
    }
    return render(request, 'squirrel_tracker/detail.html', context)


def update_latitude(request, unique_squirrel_id):
    if request.method == 'POST':
        form = LatitudeForm(request.POST)
        if form.is_valid():
            updated_latitude = form.cleaned_data['updated_latitude']
            sighting = Sighting.objects.get(unique_squirrel_id=unique_squirrel_id)
            sighting.latitude = updated_latitude
            sighting.save()
            sighting = get_object_or_404(Sighting, unique_squirrel_id=unique_squirrel_id)
            context = {
                'sighting': sighting
            }
            return redirect('squirrel_tracker:detail', unique_squirrel_id=unique_squirrel_id)
            # return render(request, 'squirrel_tracker/detail.html', context)
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({}, status=405)


def update_longitude(request, unique_squirrel_id):
    if request.method == 'POST':
        form = LongitudeForm(request.POST)
        if form.is_valid():
            updated_longitude = form.cleaned_data['updated_longitude']
            sighting = Sighting.objects.get(unique_squirrel_id=unique_squirrel_id)
            sighting.longitude = updated_longitude
            sighting.save()
            sighting = get_object_or_404(Sighting, unique_squirrel_id=unique_squirrel_id)
            context = {
                'sighting': sighting
            }
            return redirect('squirrel_tracker:detail', unique_squirrel_id=unique_squirrel_id)
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({}, status=405)


def update_shift(request, unique_squirrel_id):
    if request.method == 'POST':
        form = ShiftForm(request.POST)
        if form.is_valid():
            updated_shift = form.cleaned_data['updated_shift']
            sighting = Sighting.objects.get(unique_squirrel_id=unique_squirrel_id)
            sighting.shift = updated_shift
            sighting.save()
            sighting = get_object_or_404(Sighting, unique_squirrel_id=unique_squirrel_id)
            context = {
                'sighting': sighting
            }
            return redirect('squirrel_tracker:detail', unique_squirrel_id=unique_squirrel_id)
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({}, status=405)


def update_date(request, unique_squirrel_id):
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            updated_date = form.cleaned_data['updated_date']
            updated_date = str(updated_date)
            sighting = Sighting.objects.get(unique_squirrel_id=unique_squirrel_id)
            sighting.date = updated_date
            sighting.save()
            return redirect('squirrel_tracker:detail', unique_squirrel_id=unique_squirrel_id)
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({}, status=405)


def update_age(request, unique_squirrel_id):
    if request.method == 'POST':
        form = AgeForm(request.POST)
        if form.is_valid():
            updated_age = form.cleaned_data['updated_age']
            sighting = Sighting.objects.get(unique_squirrel_id=unique_squirrel_id)
            sighting.age = updated_age
            sighting.save()
            return redirect('squirrel_tracker:detail', unique_squirrel_id=unique_squirrel_id)
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({}, status=405)


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
        # return HttpResponse(str(form))

    return render(request, 'squirrel_tracker/add.html', {'form': form})