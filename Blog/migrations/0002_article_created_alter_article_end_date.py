# Generated by Django 4.0.5 on 2022-06-22 15:48

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 27, 15, 47, 54, 936589)),
        ),
    ]
