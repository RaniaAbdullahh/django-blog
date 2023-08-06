from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

# class FrontPage(TemplateView):
#     template_name = 'core/frontpage.html'


class About(TemplateView):
    template_name = 'core/about.html'