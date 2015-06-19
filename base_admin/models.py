from django.db import models
import datetime
# Create your models here.
class CategoryModel(models.Model):
	name = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.name

class SportCategory(models.Model):
	name = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.name

class NewsModel(models.Model):
	category = models.ForeignKey(CategoryModel)
	title = models.CharField(max_length = 200)
	body = models.TextField()
	pic = models.ImageField(null = True, blank = True)
	view = models.IntegerField(default = 0)
	news_date = models.DateTimeField(default = datetime.datetime.now())

	def __unicode__(self):
		return self.title

class SportModel(models.Model):
	sport_category = models.ForeignKey(SportCategory, null = True, blank = True)
	title = models.CharField(max_length = 200)
	body = models.TextField()
	pic = models.ImageField(null = True, blank = True)
	view = models.IntegerField(default = 0)
	sport_date = models.DateTimeField(default = datetime.datetime.now())

	def __unicode__(self):
		return self.title

class AlbumModel(models.Model):
	name = models.CharField(max_length = 200)
	album_date = models.DateTimeField(default = datetime.datetime.now())

	def __unicode__(self):
		return self.name

class PictureModel(models.Model):
	album = models.ForeignKey(AlbumModel)
	name = models.ImageField()
	pic_date = models.DateTimeField(default = datetime.datetime.now())

class VideoModel(models.Model):
	title = models.CharField(max_length = 200)
	name = models.CharField(max_length = 300)
	video_date = models.DateTimeField(default = datetime.datetime.now())

	def __unicode__(self):
		return self.title

class fModel(models.Model):
	title = models.CharField(max_length = 200)
	name = models.FileField()
	file_date = models.DateTimeField(default = datetime.datetime.now()) 
