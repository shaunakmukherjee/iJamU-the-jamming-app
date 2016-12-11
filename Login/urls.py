#Login/urls.py

from django.conf.urls import url
from . import views

# Addin an extra URL = home!
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^add/$', views.post_new, name='Post_new'),
    url(r'^edit/$', views.post_update, name='Post_update'),
    url(r'^post/new/$', views.usr_list, name='usr_list'),
    url(r'^post/$', views.gsearch, name='search'),
    url(r'^connections/$', views.Connections, name='connections'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<key>.*)/$', views.ksearch, name='ksearch'),
    url(r'^consearch/(?P<key>.*)/$', views.consearch, name='consearch'),
	url(r'^reqsearch/(?P<key>.*)/$', views.reqsearch, name='reqsearch'),
	url(r'^requests/$',views.Requests, name='requests'),
    url(r'^makereq/(?P<key>.*)/$', views.makereq, name='makereq'),
    url(r'^delreq/(?P<key>.*)/$', views.delreq, name='delreq'),
	url(r'^accept/(?P<key>.*)/$',views.accept, name='accept'),
	url(r'^deletecon/(?P<key>.*)/$', views.deletecon, name='deletecon'),
    url(r'^reqsearch/(?P<key>.*)/$', views.reqsearch, name='reqsearch'),
# URLs for Registration
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^accounts/register/complete/$', views.registration_complete, name='registration_complete'),
]
