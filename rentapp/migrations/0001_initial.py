# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-20 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rentapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=40)),
                ('rooms_available', models.CharField(max_length=60)),
                ('owner_name', models.CharField(max_length=50)),
                ('owner_phone_no', models.IntegerField(default=0)),
            ],
        ),
    ]
