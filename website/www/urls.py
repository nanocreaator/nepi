from django.conf.urls import url

from . import views

urlpatterns = [
    #root, load index by default
    url(r'^$', views.index,  name='index'),

    #/index
    url(r'^index/$', views.index,  name='index'),
    #/overview
    url(r'^overview/$', views.overview, name='overview'),
    #/platform
    url(r'^platform/$', views.platform, name='platform'),
    #/install
    url(r'^install/$', views.install, name='install'),
    #/api
    url(r'^api/$', views.api, name='api'),
    #/tutorial
    url(r'^tutorial/$', views.tutorial, name='tutorial'),
    #/contact
    url(r'^contact/$', views.contact, name='contact'),
    #/example
    url(r'^example/$', views.example, name='example'),
]
