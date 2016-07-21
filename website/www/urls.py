from django.conf.urls import url

from . import views

urlpatterns = [
    #root, load index by default
    url(r'^$', views.index),

    #/index
    url(r'^index/$', views.index),
    #/overview
    url(r'^overview/$', views.overview),
    #/platform
    url(r'^platform/$', views.platform),
    #/install
    url(r'^install/$', views.install),
    #/api
    url(r'^api/$', views.api),
    #/contact
    url(r'^contact/$', views.contact),
    #/learn
    url(r'^learn/$', views.learn),
    #/tutorial
    url(r'^tutorial/$', views.tutorial),
    url(r'^tutorials/$', views.tutorial),
    url(r'^tutorials/(?P<tutorial>[\w-]+)/$', views.tutorial),
    #/example
    url(r'^example/$', views.example),
    url(r'^examples/$', views.example),
    url(r'^examples/(?P<example>[\w-]+)/$', views.example),
    #/cases
    url(r'^case/$', views.case),
    url(r'^cases/$', views.case),
    url(r'^cases/(?P<case>[\w-]+)/$', views.case),
]
