# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 09:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_business'),
        ('hostinfo', '0003_auto_20170712_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='jifang',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.Business'),
        ),
    ]
