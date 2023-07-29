from django.conf import settings
from django.http import HttpResponse
import json


class ErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        decode = response.getvalue().decode()

        return response

    def process_exception(self, request, exception):
        return HttpResponse(json.dumps({"Errors": exception.args}),status=500)
