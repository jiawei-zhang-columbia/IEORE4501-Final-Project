from django import forms
from squirrel_tracker.models import Sighting


class UpdateForm(forms.ModelForm):

    class Meta:
        model = Sighting
        fields = [
            'latitude',
            'longitude',
            'shift',
            'date',
            'age'
        ]


class AddSightingForm(forms.ModelForm):
    class Meta:
        model = Sighting
        fields = [
            'latitude',
            'longitude',
            'unique_squirrel_id',
            'shift',
            'date',
            'age',
            'primary_fur_color',
            'location',
            'specific_location',
            'running',
            'chasing',
            'climbing',
            'eating',
            'foraging',
            'other_activities',
            'kuks',
            'quaas',
            'moans',
            'tail_flags',
            'tail_twitches',
            'approaches',
            'indifferent',
            'runs_from'
        ]
