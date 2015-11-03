# coding: utf-8

from django.conf.urls import url
from views import details

urlpatterns = [
     url(r'^$', details),
]