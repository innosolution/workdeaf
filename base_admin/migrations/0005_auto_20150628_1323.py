# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('base_admin', '0004_auto_20150512_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albummodel',
            name='album_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 28, 13, 23, 12, 82470)),
        ),
        migrations.AlterField(
            model_name='fmodel',
            name='file_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 28, 13, 23, 12, 84703)),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='news_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 28, 13, 23, 12, 80629)),
        ),
        migrations.AlterField(
            model_name='picturemodel',
            name='pic_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 28, 13, 23, 12, 83095)),
        ),
        migrations.AlterField(
            model_name='sportmodel',
            name='sport_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 28, 13, 23, 12, 81641)),
        ),
        migrations.AlterField(
            model_name='videomodel',
            name='video_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 28, 13, 23, 12, 84034)),
        ),
    ]
