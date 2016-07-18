# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-18 10:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issue_log', '0002_auto_20160718_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='is_open',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='issued_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='issue_requests_created', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
