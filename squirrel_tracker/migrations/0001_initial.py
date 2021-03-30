# Generated by Django 3.1.7 on 2021-03-30 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(help_text='Latitude')),
                ('longitude', models.FloatField(help_text='Longitude')),
                ('unique_squirrel_id', models.CharField(help_text='Unique Squirrel ID', max_length=50)),
                ('hectare', models.CharField(help_text='Hectare', max_length=10)),
                ('shift', models.CharField(help_text='Shift', max_length=10)),
                ('date', models.CharField(help_text='Date', max_length=10)),
                ('hectare_squirrel_number', models.IntegerField(default=1, help_text='Hectare Squirrel Number')),
                ('age', models.CharField(choices=[('adult', 'Adult'), ('juvenile', 'Juvenile'), ('?', '?')], help_text='Age', max_length=50)),
                ('primary_fur_color', models.CharField(default='', help_text='Primary Fur Color', max_length=100)),
                ('highlight_fur_color', models.CharField(default='', help_text='Highlight Fur Color', max_length=100)),
                ('location', models.CharField(choices=[('ground plane', 'ground plane'), ('above ground', 'above ground')], help_text='Location', max_length=50)),
                ('specific_location', models.CharField(default='', help_text='Specific Location', max_length=100)),
                ('running', models.BooleanField(help_text='Whether or not the squirrel was seen running')),
                ('chasing', models.BooleanField(help_text='Whether or not the squirrel was seen chasing')),
                ('climbing', models.BooleanField(help_text='Whether or not the squirrel was seen climbing')),
                ('eating', models.BooleanField(help_text='Whether or not the squirrel was seen eating')),
                ('foraging', models.BooleanField(help_text='Whether or not the squirrel is foraging')),
                ('other_activities', models.CharField(default='', help_text='Other Activities', max_length=200)),
                ('kuks', models.BooleanField(help_text='Whether or not the squirrel was heard kukking')),
                ('quaas', models.BooleanField(help_text='Whether or not the squirrel was heard quaaing')),
                ('moans', models.BooleanField(help_text='Whether or not the squirrel was heard moaning')),
                ('tail_flags', models.BooleanField(help_text='Whether or not the squirrel was seen flagging its tail')),
                ('tail_twitches', models.BooleanField(help_text='Whether or not the squirrel was seen twitching its tail')),
                ('approaches', models.BooleanField(help_text='Whether or not the squirrel was seen approaching human')),
                ('indifferent', models.BooleanField(help_text='Whether or not the squirrel was indifferent to human presence')),
                ('runs_from', models.BooleanField(help_text='Whether or not the squirrel was seen running away from human')),
            ],
        ),
    ]