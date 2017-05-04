# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-05-04 23:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('files', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('quantity', models.IntegerField(default=1)),
                ('visible', models.BooleanField(default=True)),
                ('zone', models.CharField(max_length=50, null=True)),
                ('shelf', models.IntegerField(null=True)),
                ('place', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('visible', models.BooleanField(default=True)),
                ('loan_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_lent')),
                ('return_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='return_date')),
                ('date_returned', models.DateTimeField(null=True, verbose_name='date_returned')),
                ('borrower', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loan_set', to=settings.AUTH_USER_MODEL)),
                ('lender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lender_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LoanItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Item')),
                ('loan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Loan')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('visible', models.BooleanField(default=True)),
                ('parent_tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children_tags', to='inventory.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(to='inventory.Tag'),
        ),
        migrations.AddField(
            model_name='item',
            name='thumbnail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='files.Image'),
        ),
    ]