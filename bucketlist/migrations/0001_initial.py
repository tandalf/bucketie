# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 14:25
from __future__ import unicode_literals

import bucketie.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BucketList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True)),
                ('description', models.TextField(default=b'')),
                ('created_at', bucketie.models.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created_at')),
                ('modified_at', bucketie.models.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified_at')),
            ],
            options={
                'ordering': ['-created_at', '-modified_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BucketListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True)),
                ('description', models.TextField(default=b'')),
                ('created_at', bucketie.models.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created_at')),
                ('modified_at', bucketie.models.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified_at')),
            ],
            options={
                'ordering': ['-created_at', '-modified_at'],
                'abstract': False,
            },
        ),
    ]
