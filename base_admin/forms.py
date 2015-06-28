from django import forms
from django.forms import ModelForm
from base_admin.models import *
#from captcha.fields import CaptchaField

class MedeeForm(ModelForm):
	class Meta:
		model = NewsModel
		fields = ('category' ,'title','body','pic')

class SportForm(ModelForm):
	class Meta: 
		model = SportModel
		fields = ('sport_category', 'title', 'body', 'pic')

class ImageForm(ModelForm):
	class Meta:
		model = PictureModel
		fields = ('album', 'name')

class VideoForm(ModelForm):
	class Meta:
		model = VideoModel
		fields = ('title', 'name')

class FileForm(ModelForm):
	class Meta:
		model = fModel
		fields = ('title', 'name')

class AlbumForm(ModelForm):
	class Meta:
		model = AlbumModel
		fields = ('name',)

#class CaptchaForm(forms.Form):
	#myfield = CharField()
#	captcha = CaptchaField(label='')
