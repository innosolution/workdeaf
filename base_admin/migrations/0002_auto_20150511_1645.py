# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('base_admin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsmodel',
            name='category',
        ),
        migrations.RemoveField(
            model_name='sportmodel',
            name='sport_category',
        ),
        migrations.AddField(
            model_name='sportmodel',
            name='category',
            field=models.ForeignKey(default=1, to='base_admin.CategoryModel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='albummodel',
            name='album_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 11, 16, 45, 4, 190000)),
        ),
        migrations.AlterField(
            model_name='fmodel',
            name='file_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 11, 16, 45, 4, 190000)),
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='news_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 11, 16, 45, 4, 190000)),
        ),
        migrations.AlterField(
            model_name='picturemodel',
            name='pic_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 11, 16, 45, 4, 190000)),
        ),
        migrations.AlterField(
            model_name='sportmodel',
            name='sport_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 11, 16, 45, 4, 190000)),
        ),
        migrations.AlterField(
            model_name='videomodel',
            name='video_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 11, 16, 45, 4, 190000)),
        ),
    ]
