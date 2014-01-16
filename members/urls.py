'''
Created on Jan 15, 2014

@author: zabeel
'''
from django.conf.urls import patterns, include, url
from members import views
urlpatterns = patterns('',
    url(r'^$', views.myFirstView, name='index'),
    url(r'^list/$', views.membersList, name='members'),
    url(r'^form/$', views.formView, name='form'),
    )