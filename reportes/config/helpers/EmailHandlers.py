from django.utils.log import AdminEmailHandler
from apps.tasks import email_deliveri


class CustomEmailHandler(AdminEmailHandler):
    
    def send_mail(self, subject, message, *args, **kwargs):
        email_deliveri.delay(subject,message)
