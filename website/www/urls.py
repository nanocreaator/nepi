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
    #/install
    url(r'^install/$', views.install, name='install'),
    #/api
    url(r'^api/$', views.api, name='api'),
    #/faq
    url(r'^faq/$', views.faq, name='faq'),
    #/contact
    url(r'^contact/$', views.contact, name='contact'),
    #/manual
    url(r'^manual/$', views.manual, name='manual'),
]
