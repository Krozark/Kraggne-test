# -*- coding: utf-8 -*-

from django.views.generic import ListView, TemplateView, DetailView
from website.models import *
from Kraggne.models import MenuItem
from django.shortcuts import get_object_or_404

class HomeView(TemplateView):
    template_name = "Kraggne/genericPage.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['page'] = get_object_or_404(MenuItem,slug='home')

        return context


