# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('base_admin', '0003_auto_20150511_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albummodel',
            name='album_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 15, 23, 29, 768000)),
        ),
        migrations.AlterField(
            model_name='fmodel',
            name='file_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 15, 23, 29, 768000)),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='news_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 15, 23, 29, 768000)),
        ),
        migrations.AlterField(
            model_name='picturemodel',
            name='pic_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 15, 23, 29, 768000)),
        ),
        migrations.AlterField(
            model_name='sportmodel',
            name='sport_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 15, 23, 29, 768000)),
        ),
        migrations.AlterField(
            model_name='videomodel',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='videomodel',
            name='video_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 15, 23, 29, 768000)),
        ),
    ]
