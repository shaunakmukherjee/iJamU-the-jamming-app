#Login/urls.py

from django.conf.urls import url
from . import views

# Addin an extra URL = home!
urlpatterns = [
# URLs for Registration
    url(r'^accounts/register/$', views.register, name='register'),
    #url(r'^accounts/register/complete/$', views.registration_complete, name='registration_complete'),
# URLs for main pages
    url(r'^$', views.home, name='home'),
]
