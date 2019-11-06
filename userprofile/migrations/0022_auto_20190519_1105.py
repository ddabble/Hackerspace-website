# Generated by Django 2.2.1 on 2019-05-19 11:05

import applications.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0021_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Brukes til reservasjonssystem i tilfelle du må kontaktes.', max_length=8, null=True, validators=[applications.validators.validate_phone_number], verbose_name='Telefonnummer'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='study',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Studieretning'),
        ),
    ]