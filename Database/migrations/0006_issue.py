# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-13 20:28
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Database', '0005_auto_20180509_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.CharField(max_length=200)),
                ('label', models.CharField(default='Help Wanted', max_length=100)),
                ('issueDescription', models.TextField()),
                ('isClosed', models.BooleanField(default=False)),
                ('issueTime', models.DateTimeField(default=datetime.datetime.now)),
                ('issueCreator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Database.Project')),
            ],
        ),
    ]