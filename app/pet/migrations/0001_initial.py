# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-10-03 14:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adoption', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=10)),
                ('age_approx', models.IntegerField()),
                ('date_recovery', models.DateField()),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adoption.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='vaccine',
            field=models.ManyToManyField(blank=True, to='pet.Vaccine'),
        ),
    ]
