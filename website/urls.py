# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
#from django.conf import settings
from website.views import *

urlpatterns=patterns('',
    url(r'^$',          HomeView.as_view(),     name='website-home'),
)
