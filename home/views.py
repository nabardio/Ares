# -*- coding: utf-8 -*-
from django.views.generic import TemplateView


class Home(TemplateView):
    """
    Home view
    """
    template_name = 'index.html'


class About(TemplateView):
    """
    About view
    """
    template_name = 'about.html'


class Contact(TemplateView):
    """
    Contact view
    """
    template_name = 'contact.html'
