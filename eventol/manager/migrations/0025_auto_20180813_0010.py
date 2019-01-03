# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-13 00:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0024_auto_20180812_2349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='type',
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.ActivityType'),
        ),
    ]
