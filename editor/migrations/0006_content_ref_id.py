# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-13 04:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0005_delete_editor'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='ref_id',
            field=models.CharField(default='1', editable=False, max_length=120, unique=True),
        ),
    ]
