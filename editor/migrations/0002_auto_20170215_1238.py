# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contentmodel',
            old_name='timestamp',
            new_name='created',
        ),
        migrations.AddField(
            model_name='contentmodel',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]