# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 04:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20160412_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='train',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='booking.Train'),
        ),
    ]
