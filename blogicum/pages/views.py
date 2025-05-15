from django.shortcuts import render
from django.views.generic import TemplateView


class RulesView(TemplateView):
    template_name = 'pages/rules.html'


class AboutView(TemplateView):
    template_name = 'pages/about.html'


def page_500(request):
    template_name = 'pages/500.html'
    return render(request, template_name, status=500)


def page_403(request, reason=''):
    template_name = 'pages/403csrf.html'
    return render(request, template_name, status=403)


def page_404(request, exception):
    template_name = 'pages/404.html'
    return render(request, template_name, status=404)
