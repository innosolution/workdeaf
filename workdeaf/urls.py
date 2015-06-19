from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # Examples:
    # url(r'^$', 'workdeaf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'workdeaf.views.Homepage'),



    url(r'^captcha/', include('captcha.urls')),
    url(r'^base_admin_site/', include(admin.site.urls)),
    #url(r'^medee/', 'workdeaf.views.medee'),
    #url(r'^uil_yvdal/', 'workdeaf.views.uil_yvdal'),
    #url(r'^deaflimp/', 'workdeaf.views.deaflimp'),
    #url(r'^zarlal/', 'workdeaf.views.zarlal'),
    #url(r'^ontsloh_hun/', 'workdeaf.views.ontsloh_hun'),
    #url(r'^sport/', 'workdeaf.views.sport'),
    #url(r'^zurag/', 'workdeaf.views.zurag_aaa'),
    #url(r'^video/', 'workdeaf.views.video'),
    #url(r'^sort_sport/(?P<sort_sport_id>\d+)', 'workdeaf.views.sort_sport'),

    #url(r'^picture/(?P<zurag_id>\d+)', 'workdeaf.views.zurag_haruulah'),
    #url(r'^get/(?P<medee_id>\d+)', 'workdeaf.views.medeelel'),

    #url(r'^get_sport/(?P<sport_id>\d+)', 'workdeaf.views.sport_medee'),
#    url(r'^admin/', include('base_admin.urls')),

    #url(r'^home/', 'workdeaf.views.home'),
    url(r'^news/', 'workdeaf.views.news'),
    url(r'^get_news/(?P<medee_id>\d+)', 'workdeaf.views.news_view'),
    url(r'^sport/', 'workdeaf.views.sport'),
    url(r'^get_sports/(?P<sport_id>\d+)', 'workdeaf.views.sports_view'),
    url(r'^album/', 'workdeaf.views.album'),
    url(r'^pictures/(?P<album_id>\d+)', 'workdeaf.views.pictures'),
    url(r'^about_us/', 'workdeaf.views.about_us'),
    url(r'^deaflymp/', 'workdeaf.views.deaflymp'),
    url(r'^support_us/', 'workdeaf.views.support_us'),
    url(r'^contact/', 'workdeaf.views.contact'),
    url(r'^news_lastest/', 'workdeaf.views.news_lastest'),
    url(r'^news_reader/', 'workdeaf.views.news_reader'),
#    url(r'^videos/', 'workdeaf.views.videos'),
    url(r'^occation/', 'workdeaf.views.occation'),
    url(r'^human/', 'workdeaf.views.human'),
    url(r'^notice/', 'workdeaf.views.notice'),

    url(r'^shooting/', 'workdeaf.views.shooting'),
    url(r'^bowling/', 'workdeaf.views.bowling'),
    url(r'^chess/', 'workdeaf.views.chess'),
    url(r'^pingpong/', 'workdeaf.views.pingpong'),
    url(r'^soccer/', 'workdeaf.views.soccer'),
    url(r'^judo/', 'workdeaf.views.judo'),
    url(r'^wrestling/', 'workdeaf.views.wrestling'),
    url(r'^ski/', 'workdeaf.views.ski'),
    url(r'^athletic/', 'workdeaf.views.athletic'),
    url(r'^swimming/', 'workdeaf.views.swimming'),
    url(r'^bicycle/', 'workdeaf.views.bicycle'),
    url(r'^basketball/', 'workdeaf.views.basketball'),
    url(r'^sport_lastest/', 'workdeaf.views.sport_lastest'),
    url(r'^sport_reader/', 'workdeaf.views.sport_reader'),
    url(r'^search/', 'workdeaf.views.search'),
    url(r'^videos/', 'workdeaf.views.videos'),
    url(r'^sent/', 'workdeaf.views.send_email'),
] +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
