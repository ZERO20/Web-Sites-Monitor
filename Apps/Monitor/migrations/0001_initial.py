# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-16 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('frequency', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Configuration',
                'verbose_name_plural': 'Configurations',
            },
        ),
        migrations.CreateModel(
            name='Monitoring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Monitoring',
                'verbose_name_plural': 'Monitoring',
            },
        ),
    ]
