# coding: utf-8

from django.conf.urls import url
from art2.views import details, press_list, my_test, latest
from django.views.generic import TemplateView

urlpatterns = [
     url(r'^details/(?P<art2id>\d+)/$', details),
     url(r'^list/$', press_list),
     url(r'^mytest/$', my_test),
     url(r'^latest/$', latest),
     url(r'^about/', TemplateView.as_view(template_name='about.html'))
]
