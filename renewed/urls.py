# coding: utf-8
from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin
from index import urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('index.urls')),
    url(r'^art1/', include('art1.urls')),
    url(r'^art2/', include('art2.urls')),
    url(r'^fav/', include('favorite.urls')),
    url(r'^model/', include('modelsform.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )