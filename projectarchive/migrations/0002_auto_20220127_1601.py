# Generated by Django 3.1.7 on 2022-01-27 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectarchive', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectarticle',
            options={'ordering': ('-pub_date',)},
        ),
        migrations.RemoveField(
            model_name='projectarticle',
            name='internal',
        ),
    ]