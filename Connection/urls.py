#Connection/urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
#URLs for requests.
    url(r'^requests/$', views.Requests, name='requests'),
    url(r'^makereq/(?P<key>.*)/$', views.makereq, name='makereq'),
    url(r'^accept/(?P<key>.*)/$', views.accept, name='accept'),
    url(r'^delreq/(?P<key>.*)/$', views.delreq, name='delreq'),
    url(r'^reqsearch/(?P<key>.*)/$', views.reqsearch, name='reqsearch'),
#URLs for connections.
    url(r'^deleteconnection/(?P<key>.*)/$',views.deleteconnection, name='deleteconnection'),
    url(r'^consearch/(?P<key>.*)/$', views.consearch, name='consearch'),
    url(r'^connections/$', views.Connections, name='connections'),
#URLs for endorsements.
    url(r'^endorsements/$', views.Endorsements, name='endorsements'),
    url(r'^endsearch/(?P<key>.*)/$', views.endsearch, name='endsearch'),
    url(r'^endorse_new/(?P<key>.*)/$', views.endorse_new, name='endorse_new'),
	url(r'^endorse_done/$',views.endorse_done, name='endorse_done'),
    url(r'^calculate/$',views.calculate, name='calculate'),
#URLs for messaging.
	url(r'^messaging/$',views.Messaging, name='messaging'),
	url(r'^email/$',views.Email,name='email'),
    url(r'^endo/$', views.endo, name='endo'),
    url(r'^endo_list/(?P<key>.*)/$', views.endo_list, name='endo_list'),
]
