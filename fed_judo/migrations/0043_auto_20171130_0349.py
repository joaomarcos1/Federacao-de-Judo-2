# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-30 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fed_judo', '0042_auto_20171130_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.ManyToManyField(to='fed_judo.TipoUsuario'),
        ),
    ]
