# Generated by Django 3.1.2 on 2020-11-02 19:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0010_auto_20201102_1915'),
        ('inventory', '0016_auto_20201102_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='stock',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Lagerbeholdning'),
        ),
        migrations.AlterField(
            model_name='item',
            name='thumbnail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='files.image', verbose_name='Bilde'),
        ),
    ]
