"""
URL configuration for reportes project.

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
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
import json




@csrf_exempt
def web(request):
    verify_token = os.getenv("VERIFY_TOKEN")
    mode = request.GET.get("hub.mode")
    challenge = request.GET.get("hub.challenge")
    token = request.GET.get("hub.verify_token")
    json_data = json.loads(request.body)


    return HttpResponse(challenge, content_type="text/plain")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("test/", include("apps.auth_user.urls")),
    # path("webhook/", web),
]
