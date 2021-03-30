from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from squirrel_tracker.models import Sighting


class Command(BaseCommand):

    help = 'Command to import squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('path_to_csv', type=str)

    def handle(self, *args, **options):
        path = options['path_to_csv']
        df = pd.read_csv(path)
        df['Age'] = df['Age'].fillna('')
        df['Primary Fur Color'] = df['Primary Fur Color'].fillna('')
        df['Highlight Fur Color'] = df['Highlight Fur Color'].fillna('')
        df['Location'] = df['Location'].fillna('')
        df['Specific Location'] = df['Specific Location'].fillna('')
        df['Other Activities'] = df['Other Activities'].fillna('')
        df['Date'] = df['Date'].astype(str)
        df.rename(columns={'X': 'Longitude', 'Y': 'Latitude'}, inplace=True)
        columns = [
            'Longitude',
            'Latitude',
            'Unique Squirrel ID',
            'Hectare',
            'Shift',
            'Date',
            'Hectare Squirrel Number',
            'Age',
            'Primary Fur Color',
            'Highlight Fur Color',
            'Location',
            'Specific Location',
            'Running',
            'Chasing',
            'Climbing',
            'Eating',
            'Foraging',
            'Other Activities',
            'Kuks',
            'Quaas',
            'Moans',
            'Tail flags',
            'Tail twitches',
            'Approaches',
            'Indifferent',
            'Runs from'
        ]
        df = df[columns].copy()
        for i in range(len(df)):
            row = df.iloc[i, :]
            s = Sighting(
                longitude=row['Longitude'],
                latitude=row['Latitude'],
                unique_squirrel_id=row['Unique Squirrel ID'],
                hectare=row['Hectare'],
                shift=row['Shift'],
                date=row['Date'],
                hectare_squirrel_number=row['Hectare Squirrel Number'],
                age=row['Age'],
                primary_fur_color=row['Primary Fur Color'],
                highlight_fur_color=row['Highlight Fur Color'],
                location=row['Location'],
                specific_location=row['Specific Location'],
                running=row['Running'],
                chasing=row['Chasing'],
                climbing=row['Climbing'],
                eating=row['Eating'],
                foraging=row['Foraging'],
                other_activities=row['Other Activities'],
                kuks=row['Kuks'],
                quaas=row['Quaas'],
                moans=row['Moans'],
                tail_flags=row['Tail flags'],
                tail_twitches=row['Tail twitches'],
                approaches=row['Approaches'],
                indifferent=row['Indifferent'],
                runs_from=row['Runs from']
            )
            s.save()
