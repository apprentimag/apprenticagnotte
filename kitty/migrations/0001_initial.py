# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 08:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import kitty.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.CharField(default=kitty.models.generate_token, max_length=16, primary_key=True, serialize=False)),
                ('admin_token', models.CharField(default=kitty.models.generate_token, max_length=16)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FinancialContribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('contributor', models.CharField(max_length=200)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitty.Budget')),
            ],
        ),
    ]
