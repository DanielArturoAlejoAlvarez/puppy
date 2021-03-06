# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-10-04 19:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YourRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_pets', models.IntegerField()),
                ('reasons', models.TextField()),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adoption.Person')),
            ],
        ),
    ]
