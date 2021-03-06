# Public Django
from django.shortcuts import render
from django.views.generic import  TemplateView


# Create your views here.
class AboutView(TemplateView):
    template_name = 'about_me/about.html'

about = AboutView.as_view()
