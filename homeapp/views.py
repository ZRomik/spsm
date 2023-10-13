from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "homeapp/home.html"

def page_not_found_view(request, exception):
    context = {
        "path": request.path
    }
    return render(request, 'homeapp/404.html', context=context, status=404)

def bad_request_view(request, exception):
    return render(request, 'homeapp/400.html', status=400)

def page_forbidden_view(request, exception):
    context={
        "path": request.path
    }
    return render(request, 'homeapp/403.html', context, 403)

def internal_error_view(request):
    return render(request, 'homeapp/500.html')