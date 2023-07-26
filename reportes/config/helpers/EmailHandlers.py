from django.utils.log import AdminEmailHandler
import logging
from celery import shared_task
from django.core.mail import EmailMessage, send_mail
import os
import requests 

API_KEY_ENV = os.getenv("API_KEY")
ID_WHATSAPP_BUSINESS_ENV = os.getenv("ID_WHATSAPP_BUSINESS")
ID_WHATSAPP_NUMBER_ENV = os.getenv("ID_WHATSAPP_NUMBER")
API_VERSION_WHATSAPP_ENV = os.getenv("API_VERSION_WHATSAPP")


@shared_task(
    bind=True,
    rate_limit="50/m",
    autoretry_for=(Exception,),
)
def email_deliveri(self, subject, message):
    mailer = EmailMessage(
        subject, message, "egresados398@gmail.com", ["neldecas12@gmail.com"]
    )
    try:
        mailer.send()
    except Exception as e:
        print(e)


class CustomEmailHandler(AdminEmailHandler):
    def send_mail(self, subject, message, *args, **kwargs):
        
        url = (
            "https://graph.facebook.com/"
            + API_VERSION_WHATSAPP_ENV
            + "/"
            + ID_WHATSAPP_NUMBER_ENV
            + "/messages"
        )
        headers = {"Authorization": API_KEY_ENV, "Content-Type": "application/json"}

        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": "57" + "3014582878",
            "type": "text",
            "text": {"preview_url": False, "body": subject},
        }

        response = requests.post(url, headers=headers, json=payload)
