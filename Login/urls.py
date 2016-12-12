#Login/urls.py

from django.conf.urls import url
from . import views

# Addin an extra URL = home!
urlpatterns = [
# URLs for Registration
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^accounts/register/complete/$', views.registration_complete, name='registration_complete'),
# URLs for main pages
    url(r'^$', views.home, name='home'),
# URLs for profile and search views
    url(r'^add/$', views.post_new, name='Post_new'),
    url(r'^edit/$', views.post_update, name='Post_update'),
    url(r'^post/new/$', views.usr_list, name='usr_list'),
    url(r'^post/$', views.gsearch, name='search'),
    url(r'^post/(?P<key>.*)/$', views.ksearch, name='ksearch'),
    url(r'^connect/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^profile/(?P<pk>\d+)/$',views.profile, name='profile'),
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
