# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-28 00:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(max_length=400),
        ),
    ]
