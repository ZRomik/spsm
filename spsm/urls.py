"""
URL configuration for spsm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler400, handler403, handler404, handler500
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

handler400 = "homeapp.views.bad_request_view"
handler403 = "homeapp.views.page_forbidden_view"
handler404 = "homeapp.views.page_not_found_view"
handler500 = "homeapp.views.internal_error_view"


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("homeapp.urls")),
    path("accounts/", include("accountapp.urls"))
]

if settings.DEBUG:
    urlpatterns.extend(
        static(
            settings.MEDIA_URL,
            document_root = settings.MEDIA_ROOT
        )
    )
