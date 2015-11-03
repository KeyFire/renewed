# coding: utf-8
from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^2003/$', views.special_case_2003),
    url(r'(\d{4})/$', views.year_archive),
    url(r'(\d{4})/(\d{2})/$', views.month_archive),
    url(r'(\d{4})/(\d{2})/(\d+)/$',views.article_detail),
)

