from django.core.context_processors import csrf
from django.conf import settings
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
#from base_admin.forms import CaptchaForm

from base_admin.models import *
def send_email(request):
	if request.POST:
		subject = '%s,%s' %(request.POST.get('name'),request.POST.get('phone'))
		message = request.POST.get('mail')
		from_email = 'uuganaaaaaa@gmail.com'
		send_mail(subject, message, from_email, ['uuganbat@innosol.mn'])
		return HttpResponseRedirect('/contact/')



def Homepage(request):
	c = {}
	c.update(csrf(request))
	a = NewsModel.objects.all().order_by('-id')[:2]
	b = SportModel.objects.all().order_by('-id')[:1]
	c['medee'] = a
	c['med'] = b
	return render_to_response('homepage.html', c)

def videos(request):
	c = {}
	c.update(csrf(request))
	a = VideoModel.objects.all().order_by('-id')
	paginator =Paginator(a, 3)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)
	c['posts'] = posts
	return render_to_response('videos.html', c)


#sdef medee(request):

#	a = NewsModel.objects.all().order_by('-news_date')
#	return render_to_response('homepage.html',{'medee' : a})

#def uil_yvdal(request):
#	medee = CategoryModel.objects.get(id = 1)
#	a = NewsModel.objects.filter(category = medee).order_by('-news_date')
#	return render_to_response('homepage.html',{'medee' : a})

#def deaflimp(request):
#	medee = CategoryModel.objects.get(id = 4)
#	a = NewsModel.objects.filter(category = medee).order_by('-news_date')
#	return render_to_response('homepage.html',{'medee' : a})

#def zarlal(request):
#	medee = CategoryModel.objects.get(id = 2)
#	a = NewsModel.objects.filter(category = medee).order_by('-news_date')
#	return render_to_response('homepage.html',{'medee' : a})

#def ontsloh_hun(request):
#	medee = CategoryModel.objects.get(id = 3)
#	a = NewsModel.objects.filter(category = medee).order_by('-news_date')
#	return render_to_response('homepage.html',{'medee' : a})

#def sport(request):
#	sp = SportCategory.objects.all()
#	a = SportModel.objects.all().order_by('-sport_date')
#	return render_to_response('sport.html',{'medee' : a, 'sp' : sp})

#def medeelel(request, medee_id = 1):
#	medee = NewsModel.objects.get(id = medee_id)
#	return render_to_response('medeelel.html', { 'medee': medee})

#def sport_medee(request, sport_id = 1):
#	medee = SportModel.objects.get(id = sport_id)
#	return render_to_response('sport_medee.html', { 'medee': medee})

#def sort_sport(request, sort_sport_id =1):
#	a = SportCategory.objects.get(id = sort_sport_id)
#	medee = SportModel.objects.filter(sport_category = a)
#	return render_to_response('sort_sport_medee.html', { 'medee': medee})

#def zurag_aaa(request):
#	a =AlbumModel.objects.all()
#	return render_to_response('zurag1.html',{ 'a':a })

#def zurag_haruulah(request, zurag_id = 1):
#	a = AlbumModel.objects.get(id = zurag_id)
#	b = PictureModel.objects.filter(album = a).order_by('pic_date')
#	return render_to_response('zurag_haruulah.html',{ 'b' : b })

#def video(request):
#	b = VideoModel.objects.all().order_by('-video_date')
#	return render_to_response('video_haruulah.html',{ 'b' : b })
#def home(request):
#	return render_to_response('index1.html')


def news(request):
	c = {}
	c.update(csrf(request))
	a = NewsModel.objects.all().order_by('-id')
	paginator =Paginator(a, 5)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)
	c['posts'] = posts
	return render_to_response('news.html', c)

def news_view(request, medee_id = 1):
	c = {}
	c.update(csrf(request))
	a = NewsModel.objects.get(id = medee_id)
	a.view = a.view + 1
	a.save()
	c['medee'] = a
	return render_to_response('medeelel.html', c)

def sport(request):
	a = SportModel.objects.all().order_by('-id')
	paginator =Paginator(a, 5)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)
	c = {}
	c.update(csrf(request))
	c['posts'] = posts
	return render_to_response('sport.html',c)

def sports_view(request, sport_id = 1):
	a = SportModel.objects.get(id = sport_id)
	a.view = a.view + 1
	a.save()
	c = {}
	c.update(csrf(request))
	c['medee'] = a
	return render_to_response('medeelel_sport.html', c)

def album(request):
	c = {}
	c.update(csrf(request))
	
	a = AlbumModel.objects.all().order_by('-id')
	c['a'] = a
	return render_to_response('album.html',c)

def pictures(request, album_id = 1):
	a = AlbumModel.objects.get(id = album_id)
	b = PictureModel.objects.filter(album = a)
	c = {}
	c.update(csrf(request))
	c['b'] = b
	return render_to_response('pictures.html', c)


def about_us(request):
#	a = AlbumModel.objects.get(id = album_id)
#	b = PictureModel.objects.filter(album = a)
	c = {}
	c.update(csrf(request))
	return render_to_response('about.html',c)
def deaflymp(request):
	a = CategoryModel.objects.get(id = 4)
	b = NewsModel.objects.filter(category = a)
	paginator =Paginator(b, 2)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)


	c = {}
	c.update(csrf(request))
	c['posts'] = posts
	return render_to_response('deaflymp.html',c)

def support_us(request):
#	a = AlbumModel.objects.get(id = album_id)
#	b = PictureModel.objects.filter(album = a)
	c = {}
	c.update(csrf(request))
	return render_to_response('support.html',c)

def contact(request):
	if request.POST:
		form = CaptchaForm(request.POST)
		if form.is_valid():
			messages.success(request, 'aaaaaaaaaaaaaaaaa')
			subject = '%s,%s' %(request.POST.get('name'),request.POST.get('phone'))
			message = request.POST.get('mail')
			from_email = 'uuganaaaaaa@gmail.com'
			send_mail(subject, message, from_email, ['enkhbayarj@mgldeafsport.mn'])
			return HttpResponseRedirect('/contact/')
#	a = AlbumModel.objects.get(id = album_id)
#	b = PictureModel.objects.filter(album = a)

	else:
		form = CaptchaForm()
		messages.success(request, 'baaaaaaaaaaa')
	c = {}
	c['form'] = form
	c['a'] = locals()
	c.update(csrf(request))
	return render_to_response('contacts.html',c)

def news_lastest(request):
	a = NewsModel.objects.all().order_by('-id')[:3]
	paginator =Paginator(a, 5)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)


	c = {}
	c.update(csrf(request))
	c['posts'] = posts
	return render_to_response('news.html',c)

def news_reader(request):
	a = NewsModel.objects.all().order_by('-view')[:3]
	paginator =Paginator(a, 5)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)


	c = {}
	c.update(csrf(request))
	c['posts'] = posts
	return render_to_response('news.html',c)

def occation(request):
	b = CategoryModel.objects.get(id = 1)
	a = NewsModel.objects.filter(category = b).order_by('news_date')
	paginator =Paginator(a, 5)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)


	c = {}
	c.update(csrf(request))
	c['posts'] = posts
	return render_to_response('news.html',c)

def human(request):
	b = CategoryModel.objects.get(id = 3)
	a = NewsModel.objects.filter(category = b).order_by('news_date')
	paginator =Paginator(a, 5)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)


	c = {}
	c.update(csrf(request))
	c['posts'] = posts
	return render_to_response('news.html',c)

def notice(request):
	b = CategoryModel.objects.get(id = 2)
	a = NewsModel.objects.filter(category = b).order_by('news_date')
	paginator =Paginator(a, 5)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)


	c = {}
	c.update(csrf(request))
	c['posts'] = posts
	return render_to_response('news.html',c)

def sport_reader(request):
	a = SportModel.objects.all().order_by('-view')[:3]
	paginator =Paginator(a, 5)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)


	c = {}
	c.update(csrf(request))
	c['posts'] = posts
	return render_to_response('sport.html',c)


def sport_lastest(request):
	a = SportModel.objects.all().order_by('-sport_date')[:3]
	paginator =Paginator(a, 5)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)


	c = {}
	c.update(csrf(request))
	c['posts'] = posts
	return render_to_response('sport.html',c)





def basketball(request):
	b = SportCategory.objects.get(id = 8)
	a = SportModel.objects.filter(sport_category = b).order_by('sport_date')
	paginator =Paginator(a, 5)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)


	c = {}
	c.update(csrf(request))
	c['posts'] = posts
	return render_to_response('sport.html',c)
def soccer(request):
	b = SportCategory.objects.get(id = 9)
	a = SportModel.objects.filter(sport_category = b).order_by('sport_date')
	paginator =Paginator(a, 5)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)


	c = {}
	c.update(csrf(request))
	c['posts'] = posts
	return render_to_response('sport.html',c)
def shooting(request):
	b = SportCategory.objects.get(id = 1)
	a = SportModel.objects.filter(sport_category = b).order_by('sport_date')
	paginator =Paginator(a, 5)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)


	c = {}
	c.update(csrf(request))
	c['posts'] = posts
	return render_to_response('sport.html',c)
def bowling(request):
	b = SportCategory.objects.get(id = 2)
	a = SportModel.objects.filter(sport_category = b).order_by('sport_date')
	paginator =Paginator(a, 5)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)


	c = {}
	c.update(csrf(request))
	c['posts'] = posts
	return render_to_response('sport.html',c)
def bicycle(request):
	b = SportCategory.objects.get(id = 3)
	a = SportModel.objects.filter(sport_category = b).order_by('sport_date')
	paginator =Paginator(a, 5)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)


	c = {}
	c.update(csrf(request))
	c['posts'] = posts
	return render_to_response('sport.html',c)
def judo(request):
	b = SportCategory.objects.get(id = 4)
	a = SportModel.objects.filter(sport_category = b).order_by('sport_date')
	paginator =Paginator(a, 5)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)


	c = {}
	c.update(csrf(request))
	c['posts'] = posts
	return render_to_response('sport.html',c)
def wrestling(request):
	b = SportCategory.objects.get(id = 5)
	a = SportModel.objects.filter(sport_category = b).order_by('sport_date')
	paginator =Paginator(a, 5)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)


	c = {}
	c.update(csrf(request))
	c['posts'] = posts
	return render_to_response('sport.html',c)
def ski(request):
	b = SportCategory.objects.get(id = 6)
	a = SportModel.objects.filter(sport_category = b).order_by('sport_date')
	paginator =Paginator(a, 5)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)


	c = {}
	c.update(csrf(request))
	c['posts'] = posts
	return render_to_response('sport.html',c)

def swimming(request):
	b = SportCategory.objects.get(id = 7)
	a = SportModel.objects.filter(sport_category = b).order_by('sport_date')
	paginator =Paginator(a, 5)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)


	c = {}
	c.update(csrf(request))
	c['posts'] = posts
	return render_to_response('sport.html',c)

def athletic(request):
	b = SportCategory.objects.get(id = 10)
	a = SportModel.objects.filter(sport_category = b).order_by('sport_date')
	paginator =Paginator(a, 5)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)


	c = {}
	c.update(csrf(request))
	c['posts'] = posts
	return render_to_response('sport.html',c)

def chess(request):
	b = SportCategory.objects.get(id = 11)
	a = SportModel.objects.filter(sport_category = b).order_by('sport_date')
	paginator =Paginator(a, 5)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)
	c = {}
	c.update(csrf(request))
	c['posts'] = posts
	return render_to_response('sport.html',{'posts' : posts})			

def pingpong(request):
	c = {}
	c.update(csrf(request))
	b = SportCategory.objects.get(id = 12)
	a = SportModel.objects.filter(sport_category = b).order_by('sport_date')
	paginator =Paginator(a, 5)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1

	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)

	c['posts'] = posts


	return render_to_response('sport.html',c)									


def search(request):
	search_text = request.POST.get('search_text')
	if search_text != '':
		news = NewsModel.objects.filter(title__contains = search_text).order_by('-id')
	else:
		news = ''
	c = {}
	c.update(csrf(request))
	c['posts'] = news
	return render_to_response('search.html', c)