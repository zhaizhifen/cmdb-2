# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-17 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostinfo', '0008_auto_20170717_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='beizhu',
            field=models.CharField(max_length=1000, null=True, verbose_name='CPU'),
        ),
    ]
