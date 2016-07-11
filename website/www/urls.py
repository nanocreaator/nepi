from django.conf.urls import url

from . import views

urlpatterns = [
    #root, load index by default
    url(r'^$', views.index,  name='index'),

    #/index
    url(r'^index/$', views.index,  name='index'),
    #/overview
    url(r'^overview/$', views.overview, name='overview'),
    #/source
    url(r'^source/$', views.source, name='source'),
    #/get_started
    url(r'^get_started/$', views.get_started, name='get_started'),
    #/api
    url(r'^api/$', views.api, name='api'),
    #/download
    url(r'^download/$', views.download, name='download'),
    #/contact
    url(r'^contact/$', views.contact, name='contact'),
    #/manual
    url(r'^manual/$', views.manual, name='manual'),
]
