from django import forms


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