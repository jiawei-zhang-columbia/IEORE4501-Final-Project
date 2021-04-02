from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse

from .models import Sighting
from .forms import LatitudeForm
from .forms import LongitudeForm
from .forms import ShiftForm
from .forms import DateForm


def index(request):

    def parse_date(date):
        month = date[:2]
        day = date[2:4]
        year = date[4:]

        date = month + '-' + day + '-' + year

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