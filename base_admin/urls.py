from django.conf.urls import url, patterns

urlpatterns = patterns('',
    url(r'^$', 'base_admin.views.admin', name = 'admin'),
    url(r'^medee/', 'base_admin.views.medee', name = 'medee'),
    url(r'^zurag_zasah/', 'base_admin.views.zurag_admin', name = 'zurag'),
    url(r'^video/', 'base_admin.views.video', name = 'video'),
    url(r'^file/', 'base_admin.views.file'),
    url(r'^sport/', 'base_admin.views.sport'),
    url(r'^get/(?P<medee_id>\d+)/', 'base_admin.views.news'),
    url(r'^medee_nemeh/', 'base_admin.views.medee_nemeh'),
    url(r'^zurag_nemeh/', 'base_admin.views.zurag_nemeh'),
    url(r'^album_nemeh/', 'base_admin.views.album_nemeh'),
    url(r'^sport_nemeh/', 'base_admin.views.sport_nemeh'),
    url(r'^video_nemeh/', 'base_admin.views.video_nemeh'),
	)