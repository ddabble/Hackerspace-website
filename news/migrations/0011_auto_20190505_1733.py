# Generated by Django 2.0.10 on 2019-05-05 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20190430_2023'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('time_start',), 'permissions': (('can_see_attendees', 'Can see attending, waitlist, register meetup in a event'),)},
        ),
    ]