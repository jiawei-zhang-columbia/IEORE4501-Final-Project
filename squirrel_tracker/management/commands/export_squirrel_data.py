from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from squirrel_tracker.models import Sighting


class Command(BaseCommand):

    help = 'Command to export squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('path_to_csv', type=str)

    def handle(self, *args, **options):
        sightings = Sighting.objects.all()
        results = []
        for i in range(len(sightings)):
            sighting = sightings[i]

            longitude = sighting.longitude
            latitude = sighting.latitude
            unique_squirrel_id = sighting.unique_squirrel_id
            hectare = sighting.hectare
            shift = sighting.shift
            date = sighting.date
            hectare_squirrel_number = sighting.hectare_squirrel_number
            age = sighting.age
            primary_fur_color = sighting.primary_fur_color
            highlight_fur_color = sighting.highlight_fur_color
            location = sighting.location
            specific_location = sighting.specific_location
            running = sighting.running
            chasing = sighting.chasing
            climbing = sighting.climbing
            eating = sighting.eating
            foraging = sighting.foraging
            other_activities = sighting.other_activities
            kuks = sighting.kuks
            quaas = sighting.quaas
            moans = sighting.moans
            tail_flags = sighting.tail_flags
            tail_twitches = sighting.tail_twitches
            approaches = sighting.approaches
            indifferent = sighting.indifferent
            runs_from = sighting.runs_from

            result = dict()
            result['Longitude'] = longitude
            result['Latitude'] = latitude
            result['Unique Squirrel ID'] = unique_squirrel_id
            result['Hectare'] = hectare
            result['Shift'] = shift
            result['Date'] = date
            result['Hectare Squirrel Number'] = hectare_squirrel_number
            result['Age'] = age
            result['Primary Fur Color'] = primary_fur_color
            result['Highlight Fur Color'] = highlight_fur_color
            result['Location'] = location
            result['Specific Location'] = specific_location
            result['Running'] = running
            result['Chasing'] = chasing
            result['Climbing'] = climbing
            result['Eating'] = eating
            result['Foraging'] = foraging
            result['Other Activities'] = other_activities
            result['Kuks'] = kuks
            result['Quaas'] = quaas
            result['Moans'] = moans
            result['Tail flags'] = tail_flags
            result['Tail twitches'] = tail_twitches
            result['Approaches'] = approaches
            result['Indifferent'] = indifferent
            result['Runs from'] = runs_from

            results.append(result)

        df = pd.DataFrame(results)
        df.to_csv(options['path_to_csv'])