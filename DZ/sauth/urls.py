from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.conf.urls import url

from sauth.views import register
from sauth.views import logout_handler

urlpatterns = [
    url('^login', login, name='login'),
    # url('^auth', ''),
    url('^logout', logout_handler, name='logout'),
    url('^', register, name='authentication'),
]
