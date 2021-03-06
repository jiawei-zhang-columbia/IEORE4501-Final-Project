# Generated by Django 3.1.7 on 2021-04-05 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel_tracker', '0004_auto_20210405_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='age',
            field=models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), ('?', '?')], help_text='Age', max_length=50),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='location',
            field=models.CharField(blank=True, choices=[('Ground Plane', 'ground plane'), ('Above Ground', 'above ground')], help_text='Location', max_length=50),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='shift',
            field=models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], help_text='Shift', max_length=10),
        ),
    ]
