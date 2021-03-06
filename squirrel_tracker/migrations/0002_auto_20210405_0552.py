# Generated by Django 3.1.7 on 2021-04-05 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='age',
            field=models.CharField(blank=True, choices=[('adult', 'Adult'), ('juvenile', 'Juvenile'), ('?', '?')], help_text='Age', max_length=50),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='date',
            field=models.IntegerField(help_text='Date'),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='highlight_fur_color',
            field=models.CharField(blank=True, default='', help_text='Highlight Fur Color', max_length=100),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='location',
            field=models.CharField(blank=True, choices=[('ground plane', 'ground plane'), ('above ground', 'above ground')], help_text='Location', max_length=50),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='other_activities',
            field=models.CharField(blank=True, help_text='Other Activities', max_length=200),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='primary_fur_color',
            field=models.CharField(blank=True, help_text='Primary Fur Color', max_length=100),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='shift',
            field=models.CharField(choices=[('am', 'AM'), ('pm', 'PM')], help_text='Shift', max_length=10),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='specific_location',
            field=models.CharField(blank=True, default='', help_text='Specific Location', max_length=100),
        ),
    ]
