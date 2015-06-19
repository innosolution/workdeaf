from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from base_admin.models import *
from base_admin.forms import *

# Create your views here.
def admin(request):
	return render_to_response('admin.html')

def medee(request):
	cat = CategoryModel.objects.all()
	medees = NewsModel.objects.all()
	return render_to_response('medee.html', {'medees': medees, 'cat': cat})


def zurag_admin(request):
	album = AlbumModel.objects.all()
	zurag = PictureModel.objects.all()
	return render_to_response('zurag.html',{'zurag': zurag, 'album' : album})
def video(request):
	video = VideoModel.objects.all()
	return render_to_response('video.html',{'video':video})
def file(request):
#	a = FileModel.objects.all()
	fil = fModel.objects.all()
	return render_to_response('file.html',{ 'fil' : fil } )

def sport(request):
#	a = FileModel.objects.all()
	sport = SportModel.objects.all()
	return render_to_response('sport_admin.html',{ 'sport' : sport } )

def news(request, medee_id=1):
	cat = CategoryModel.objects.all()
	medee = CategoryModel.objects.get(id = medee_id)
	a = NewsModel.objects.filter(category = medee)
	return render_to_response('news.html', {'a' : a,  'cat': cat})

def medee_nemeh(request):
	if request.POST:
		form = MedeeForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/admin/')
	else:
		form = MedeeForm()
	c = {}
	c.update(csrf(request))
	c['form'] = form
	return render_to_response('medee_nemeh.html', c)

def zurag_nemeh(request):
	if request.POST:
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/admin/')
	else:
		form = ImageForm()
	c = {}
	c.update(csrf(request))
	c['form'] = form
	return render_to_response('zurag_nemeh.html', c)

def album_nemeh(request):
	if request.POST:
		form = AlbumForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/admin/')
	else:
		form = AlbumForm()
	c = {}
	c.update(csrf(request))
	c['form'] = form
	return render_to_response('album_nemeh.html', c)

def sport_nemeh(request):
	if request.POST:
		form = SportForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/admin/')
	else:
		form = SportForm()
	c = {}
	c.update(csrf(request))
	c['form'] = form
	return render_to_response('sport_nemeh.html', c)

def video_nemeh(request):
	if request.POST:
		form = VideoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/admin/')
	else:
		form = VideoForm()
	c = {}
	c.update(csrf(request))
	c['form'] = form
	return render_to_response('video_nemeh.html', c)
