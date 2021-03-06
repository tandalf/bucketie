# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 16:09
from __future__ import unicode_literals

import bucketlist.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bucketlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucketlist',
            name='owner',
            field=models.ForeignKey(default=bucketlist.models.default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bucketlistitem',
            name='assigned_user',
            field=models.ForeignKey(default=bucketlist.models.default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bucketlistitem',
            name='bucketlist',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='bucketlist.BucketList'),
        ),
        migrations.AddField(
            model_name='bucketlistitem',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
