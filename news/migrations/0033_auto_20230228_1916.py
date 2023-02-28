# Generated by Django 3.2.17 on 2023-02-28 19:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0032_alter_article_main_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='responsible',
        ),
        migrations.AddField(
            model_name='event',
            name='responsible',
            field=models.ManyToManyField(related_name='responsible', to=settings.AUTH_USER_MODEL, verbose_name='Arrangementansvarlig'),
        ),
    ]
