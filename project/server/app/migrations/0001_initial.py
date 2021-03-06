# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='название')),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'categories',
                'verbose_name_plural': 'категории',
                'verbose_name': 'категория',
            },
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('in_stock', models.BooleanField(db_index=True, default=True, verbose_name='в наличии')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Category', verbose_name='категория(и)')),
            ],
            options={
                'db_table': 'goods',
                'verbose_name_plural': 'товары',
                'verbose_name': 'товар',
            },
        ),
    ]
