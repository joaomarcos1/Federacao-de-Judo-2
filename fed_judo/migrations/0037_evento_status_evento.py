# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 23:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fed_judo', '0036_statuseventos'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='status_evento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fed_judo.StatusEventos'),
        ),
    ]
