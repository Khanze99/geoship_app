# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-11-02 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geoships_info_app', '0003_auto_20191102_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='vessel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='history', to='geoships_info_app.Vessel'),
        ),
    ]