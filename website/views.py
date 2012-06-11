# -*- coding: utf-8 -*-

from django.views.generic import ListView, TemplateView, DetailView
from website.models import *


class HomeView(TemplateView):
    template_name = 'website/home.html'
