# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-30 19:43
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0029_auto_20180929_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='customFields',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
