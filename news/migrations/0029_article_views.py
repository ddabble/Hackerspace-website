# Generated by Django 3.2.7 on 2021-09-23 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0028_auto_20210210_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Sidevisninger'),
        ),
    ]