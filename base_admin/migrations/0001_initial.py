# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('album_date', models.DateTimeField(default=datetime.datetime(2015, 5, 11, 16, 40, 41, 73000))),
            ],
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='fModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('name', models.FileField(upload_to=b'')),
                ('file_date', models.DateTimeField(default=datetime.datetime(2015, 5, 11, 16, 40, 41, 77000))),
            ],
        ),
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('pic', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('view', models.IntegerField(default=0)),
                ('news_date', models.DateTimeField(default=datetime.datetime(2015, 5, 11, 16, 40, 41, 71000))),
                ('category', models.ForeignKey(to='base_admin.CategoryModel')),
            ],
        ),
        migrations.CreateModel(
            name='PictureModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.ImageField(upload_to=b'')),
                ('pic_date', models.DateTimeField(default=datetime.datetime(2015, 5, 11, 16, 40, 41, 74000))),
                ('album', models.ForeignKey(to='base_admin.AlbumModel')),
            ],
        ),
        migrations.CreateModel(
            name='SportCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SportModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('pic', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('view', models.IntegerField(default=0)),
                ('sport_date', models.DateTimeField(default=datetime.datetime(2015, 5, 11, 16, 40, 41, 72000))),
                ('sport_category', models.ForeignKey(blank=True, to='base_admin.SportCategory', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VideoModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('name', models.FileField(upload_to=b'')),
                ('video_date', models.DateTimeField(default=datetime.datetime(2015, 5, 11, 16, 40, 41, 76000))),
            ],
        ),
    ]
