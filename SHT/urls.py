#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'yw'

from django.conf.urls import url,patterns
from data_mining import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)