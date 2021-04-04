from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class LatitudeForm(forms.Form):
    updated_latitude = forms.FloatField()


class LongitudeForm(forms.Form):
    updated_longitude = forms.FloatField()


class ShiftForm(forms.Form):
    updated_shift = forms.CharField(
        max_length=10
    )


class DateForm(forms.Form):
    updated_date = forms.CharField(
        max_length=10
    )


class AgeForm(forms.Form):
    updated_age = forms.CharField(
        max_length=10
    )


class AddSightingForm(forms.Form):
    latitude = forms.FloatField(
        required=True,
        error_messages={'required': 'Latitude Field is required'}
    )

    longitude = forms.FloatField(
        required=True,
        error_messages={'required': 'Longitude Field is required'}
    )
    unique_squirrel_id = forms.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                r'^[0-9]+[A-Z]-[AP]M-[0-9]{4}-[0-9]{2}$',
                message="Incorrect Format of unique squirrel id",
                code='invalid'
            )
        ],
        error_messages={'required': 'Unique Squirrel ID is required'}
    )
    shift = forms.CharField(
        max_length=10,
        error_messages={'required': 'Shift Field is required'}
    )
    date = forms.CharField(
        max_length=10,
        error_messages={'required': 'Date Field is required'}
    )
    age = forms.CharField(
        max_length=10,
        error_messages={'required': 'Age Field is required'}
    )
