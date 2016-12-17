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
#URLs for messaging.
	url(r'^messaging/$',views.Messaging, name='messaging'),
	url(r'^email/$',views.Email,name='email'),
]