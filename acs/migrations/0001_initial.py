# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-20 18:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
            ],
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
