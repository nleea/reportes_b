from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
import json
from apps.tasks import email_deliveri


def test(request):
    resp = HttpResponse("Hello")
    resp.status_code = 200
    return resp
    # raise Exception("sds")