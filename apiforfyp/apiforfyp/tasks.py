from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_special_offers(email, subject, message):
    try:
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, [email], fail_silently=False)
        print("Special offers email sent successfully!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")