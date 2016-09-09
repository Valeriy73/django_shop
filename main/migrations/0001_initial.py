# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('alias', models.SlugField(verbose_name='Alias категории')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Название товара')),
                ('price', models.IntegerField(verbose_name='Цена', default=0)),
                ('image', models.CharField(max_length=255, verbose_name='Ссылка на картинку')),
                ('alias', models.SlugField(verbose_name='Alias товара')),
                ('category', models.ForeignKey(to='main.Category')),
            ],
        ),
    ]
