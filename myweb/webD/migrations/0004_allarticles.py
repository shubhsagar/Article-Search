# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-24 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webD', '0003_fruit'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllArticles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Link', models.CharField(max_length=30)),
            ],
        ),
    ]