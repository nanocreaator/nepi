from django.conf.urls import url

from . import views

urlpatterns = [
    #root, load index by default
    url(r'^$', views.index,  name='index'),

    #/index
    url(r'^index/$', views.index,  name='index'),
    #/source
    url(r'^source/$', views.source, name='source'),
]
