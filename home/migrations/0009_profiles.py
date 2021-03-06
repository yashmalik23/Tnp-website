# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-20 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_delete_profiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('regn_no', models.CharField(max_length=250)),
                ('CGPA', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=250)),
                ('skill1', models.CharField(max_length=250)),
                ('skill2', models.CharField(max_length=250)),
                ('skill3', models.CharField(max_length=250)),
                ('pic', models.FileField(upload_to='')),
            ],
        ),
    ]
