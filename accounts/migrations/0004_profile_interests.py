# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-21 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='interests',
            field=models.CharField(max_length=40, null=True),
        ),
    ]