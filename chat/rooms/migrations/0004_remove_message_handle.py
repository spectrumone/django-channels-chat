# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 15:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_message_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='handle',
        ),
    ]
