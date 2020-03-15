# Generated by Django 3.0.2 on 2020-03-04 20:07

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0028_auto_20200211_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='skills',
        ),
        migrations.AlterField(
            model_name='termsofservice',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]
