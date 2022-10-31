from celery import shared_task
from django.core.mail import send_mail
from time import sleep


@shared_task
def login_mail(subject,message,from_email,recipient_list):
    # sleep(20000)
    send_mail(
    subject,
    message,
    from_email,
    recipient_list,
    fail_silently=False,
)
    print("Mail Sent")
    return None