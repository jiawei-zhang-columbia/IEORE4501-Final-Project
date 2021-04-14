from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import RegexValidator


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
        unique=True,
        validators=[
            RegexValidator(
                '^[0-9]+[A-Z]-[AP]M-[0-9]{4}-[0-9]{2}$',
                message='Incorrect format of Unique Squirrel ID',
                code='invalid_id'
            )
        ]
    )

    hectare = models.CharField(
        max_length=10,
        help_text=_('Hectare')
    )

    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = [
        (AM, 'AM'),
        (PM, 'PM')
    ]
    shift = models.CharField(
        max_length=10,
        help_text=_('Shift'),
        choices=SHIFT_CHOICES
    )

    date = models.DateField(
        help_text=_('Date')
    )

    hectare_squirrel_number = models.IntegerField(
        default=1,
        help_text=_('Hectare Squirrel Number')
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
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
        blank=True
    )

    primary_fur_color = models.CharField(
        max_length=100,
        help_text='Primary Fur Color',
        blank=True
    )

    highlight_fur_color = models.CharField(
        max_length=100,
        help_text='Highlight Fur Color',
        default='',
        blank=True
    )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'

    LOCATION_CHOICES = [
        (GROUND_PLANE, _('ground plane')),
        (ABOVE_GROUND, _('above ground')),
    ]

    location = models.CharField(
        max_length=50,
        help_text='Location',
        choices=LOCATION_CHOICES,
        blank=True
    )

    specific_location = models.CharField(
        max_length=100,
        help_text='Specific Location',
        default='',
        blank=True
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
        blank=True
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
