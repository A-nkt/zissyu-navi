from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'about_me/about.html'


about = AboutView.as_view()
