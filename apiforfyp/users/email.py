from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .models import CustomUser
from random import randint


def send_otp(email):
    try:
        subject = f"🎁 Special Delivery: Your Account Verification Code!"
        otp = randint(100000, 999999)
        message = f"Hello there!\n\nWelcome to My Gym Buddy - your ultimate fitness companion! 🏋️‍♂️\n\nThank you for choosing us to help you on your fitness journey. Your One-Time Password (OTP) for account verification is: {otp}.\n\nWe're pumped to have you on board! Use this OTP to confirm your account and start sweating it out with our amazing features.\n\nIf you didn't request this OTP, no worries - simply ignore this message.\n\nStay motivated and keep pushing your limits!\n\nBest regards,\nThe My Gym Buddy Team"

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
