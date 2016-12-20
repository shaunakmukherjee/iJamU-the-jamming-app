#Profile/urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
# URLs for profile and search views
    url(r'^add/$', views.post_new, name='post_new'),
    url(r'^edit/$', views.post_update, name='post_update'),
    url(r'^post/new/$', views.usr_list, name='usr_list'),
    url(r'^post/$', views.gsearch, name='search'),
    url(r'^post/(?P<key>.*)/$', views.ksearch, name='ksearch'),
    url(r'^connect/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^profile/(?P<pk>\d+)/$',views.profile, name='profile'),
    url(r'^userprofile/$',views.userprofile, name='userprofile'),
]
