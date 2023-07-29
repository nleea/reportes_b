from celery import shared_task
from django.core.mail import EmailMessage
from variables import ADMINS
import logging

logger = logging.Logger(__name__)

@shared_task(
    bind=True,
    rate_limit="50/m",
    autoretry_for=(Exception,),
)
def email_deliveri(self, subject, message):
    
    mailer = EmailMessage(
        subject, message, "egresados398@gmail.com", [x[1] for x in ADMINS]
    )
    try:
        mailer.send()
    except Exception as e:
        print(e)

