# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-17 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostinfo', '0007_remove_history_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='cpu_core',
            field=models.CharField(max_length=50, null=True, verbose_name='CPU'),
        ),
        migrations.AddField(
            model_name='host',
            name='model_name',
            field=models.CharField(max_length=50, null=True, verbose_name='型号'),
        ),
        migrations.AddField(
            model_name='host',
            name='password',
            field=models.CharField(max_length=50, null=True, verbose_name='密码'),
        ),
        migrations.AddField(
            model_name='host',
            name='port',
            field=models.CharField(max_length=50, null=True, verbose_name='端口'),
        ),
        migrations.AddField(
            model_name='host',
            name='sn',
            field=models.CharField(max_length=50, null=True, verbose_name='SN'),
        ),
        migrations.AddField(
            model_name='host',
            name='username',
            field=models.CharField(max_length=50, null=True, verbose_name='登陆用户'),
        ),
        migrations.AlterField(
            model_name='host',
            name='hostname',
            field=models.CharField(max_length=50, verbose_name='主机编号'),
        ),
    ]
