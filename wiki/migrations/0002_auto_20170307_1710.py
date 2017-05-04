# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 16:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlpath',
            name='article',
            field=models.ForeignKey(help_text='This field is automatically updated, but you need to populate it when creating a new URL path.', on_delete=django.db.models.deletion.CASCADE, to='wiki.Article', verbose_name='article'),
        ),
    ]