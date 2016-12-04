#Login/urls.py

from django.conf.urls import url
from . import views

# Addin an extra URL = home!
urlpatterns = [
    url(r'^$', views.home, name='home'),
# URl to access data of all the user
    url(r'^post/new/$', views.usr_list, name='usr_list'),
# Search redirects to this URL 
    url(r'^post/$', views.profilesearch, name='profilesearch'),
# Returns details of the selected user 
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
# Returns search results
    url(r'^post/(?P<key>.*)/$', views.profile, name='profile'),
# URLs for Registration
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^accounts/register/complete/$', views.registration_complete, name='registration_complete'),
]
