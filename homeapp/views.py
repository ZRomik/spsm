from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "homeapp/home.html"

def page_not_found_view(request, exception):
    context = {
        "path": request.path
    }
    return render(request, 'homeapp/404.html', context=context, status=404)