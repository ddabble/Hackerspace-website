# Generated by Django 3.1.2 on 2021-03-22 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20210322_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='color',
            field=models.CharField(default='hs-yellow', help_text='Bakgrunnsfargen til banneret som en hex-farge. hs-green, hs-yellow og hs-red støttes også som presets.', max_length=10, verbose_name='bannercolor'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='site',
            field=models.CharField(default='*', help_text="Det interne navnet på URL-stien til sidene som banneret skal dukke opp på. Wildcard (*) støttes. F.eks. er '*' ALLE sider, 'inventory:*' er alle lagersider.", max_length=250, verbose_name='bannersider'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='text',
            field=models.TextField(default='Sample Text', help_text='Tekst som vises i banneret.', max_length=1000, verbose_name='bannertext'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='text_color',
            field=models.CharField(default='hs-black', help_text='Tekstfargen på banneret. hs-white og hs-black støttes som presets.', max_length=10, verbose_name='bannertextcolor'),
        ),
    ]
