from django.db import models
from django.utils.translation import gettext as _


class Sighting(models.Model):

    latitude = models.FloatField(
        help_text='Latitude'
    )

    longitude = models.FloatField(
        help_text='Longitude'
    )

    unique_squirrel_id = models.CharField(
        max_length=50,
        help_text=_('Unique Squirrel ID'),
    )

    hectare = models.CharField(
        max_length=10,
        help_text=_('Hectare')
    )

    shift = models.CharField(
        max_length=10,
        help_text=_('Shift')
    )

    date = models.CharField(
        max_length=10,
        help_text=_('Date')
    )

    hectare_squirrel_number = models.IntegerField(
        default=1,
        help_text=_('Hectare Squirrel Number')
    )

    ADULT = 'adult'
    JUVENILE = 'juvenile'
    QUESTION_MARK = '?'

    AGE_CHOICES = [
        (ADULT, _('Adult')),
        (JUVENILE, _('Juvenile')),
        (QUESTION_MARK, _('?')),
    ]

    age = models.CharField(
        max_length=50,
        help_text='Age',
        choices=AGE_CHOICES,
    )

    primary_fur_color = models.CharField(
        max_length=100,
        help_text='Primary Fur Color',
        default=''
    )

    highlight_fur_color = models.CharField(
        max_length=100,
        help_text='Highlight Fur Color',
        default=''
    )

    GROUND_PLANE = 'ground plane'
    ABOVE_GROUND = 'above ground'

    LOCATION_CHOICES = [
        (GROUND_PLANE, _('ground plane')),
        (ABOVE_GROUND, _('above ground')),
    ]

    location = models.CharField(
        max_length=50,
        help_text='Location',
        choices=LOCATION_CHOICES,
    )

    specific_location = models.CharField(
        max_length=100,
        help_text='Specific Location',
        default=''
    )

    running = models.BooleanField(
        help_text='Whether or not the squirrel was seen running'
    )

    chasing = models.BooleanField(
        help_text='Whether or not the squirrel was seen chasing'
    )

    climbing = models.BooleanField(
        help_text='Whether or not the squirrel was seen climbing'
    )

    eating = models.BooleanField(
        help_text='Whether or not the squirrel was seen eating'
    )

    foraging = models.BooleanField(
        help_text='Whether or not the squirrel is foraging'
    )

    other_activities = models.CharField(
        max_length=200,
        help_text='Other Activities',
        default=''
    )

    kuks = models.BooleanField(
        help_text="Whether or not the squirrel was heard kukking"
    )

    quaas = models.BooleanField(
        help_text="Whether or not the squirrel was heard quaaing"
    )

    moans = models.BooleanField(
        help_text='Whether or not the squirrel was heard moaning'
    )

    tail_flags = models.BooleanField(
        help_text="Whether or not the squirrel was seen flagging its tail"
    )

    tail_twitches = models.BooleanField(
        help_text="Whether or not the squirrel was seen twitching its tail"
    )

    approaches = models.BooleanField(
        help_text="Whether or not the squirrel was seen approaching human"
    )

    indifferent = models.BooleanField(
        help_text="Whether or not the squirrel was indifferent to human presence"
    )

    runs_from = models.BooleanField(
        help_text='Whether or not the squirrel was seen running away from human'
    )