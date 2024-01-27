from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .models import CustomUser
from random import randint


def send_otp(email):
    try:
        subject = f"Your account verification email"
        otp = randint(1000, 9999)
        message = f"OTP for verification is {otp}"
        email_from = settings.EMAIL_HOST
        send_mail(subject, message, email_from, [email], fail_silently=False)

        user_obj = CustomUser.objects.get(email=email)
        user_obj.otp = otp
        user_obj.save()

    except BadHeaderError as e:
        print(f"Error sending email: {e}")
    except CustomUser.DoesNotExist as e:
        print(f"Error updating user object: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
