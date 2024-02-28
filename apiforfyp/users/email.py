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


def send_welcome_mail(email, username):
    try:
        subject = "Welcome to My Gym Buddy, " + username + "!"
        message = (
            "Dear "
            + username
            + ",\n\nWelcome to My Gym Buddy! We're thrilled to have you join our fitness community.\n\nGet ready to crush your fitness goals together!\n\nBest regards,\nThe My Gym Buddy Team"
        )
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, [email], fail_silently=False)
        print("Welcome email sent successfully!")

    except BadHeaderError as e:
        print(f"Error sending email: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def send_dummy_mail(email, subject,message):
    try:
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, [email], fail_silently=False)
        print("Dummy email sent successfully!")
    except BadHeaderError as e:
        print(f"Error sending email: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def send_special_offers(email):
    try:
        subject = "Exclusive Special Offers Just for You!"
        message = "Dear valued customer,\n\nWe're excited to offer you exclusive special offers available only for our loyal customers like you.\n\nVisit our website or app now to discover these amazing deals!\n\nBest regards,\nThe Team"
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, [email], fail_silently=False)
        print("Special offers email sent successfully!")

    except BadHeaderError as e:
        print(f"Error sending email: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def send_password_change_otp(email, username):
    try:
        subject = f""
        otp = randint(100000, 999999)
        message = f"Hello there!\n\nWe've received a request to change your password. Your One-Time Password (OTP) for password change is: {otp}.\n\nIf you didn't request this OTP, no worries - simply ignore this message.\n\nStay safe and secure!\n\nBest regards,\nThe My Gym Buddy Team"

        email_from = settings.EMAIL_HOST
        send_mail(subject, message, email_from, [email], fail_silently=False)

    except BadHeaderError as e:
        print(f"Error sending email: {e}")
    except CustomUser.DoesNotExist as e:
        print(f"Error updating user object: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def send_password_change_otp(email, username):
    try:
        subject = f"Password Change OTP for {username}"
        otp = randint(100000, 999999)
        message = f"Hello {username}!\n\nWe've received a request to change your password. Your One-Time Password (OTP) for password change is: {otp}.\n\nIf you didn't request this OTP, no worries - simply ignore this message.\n\nStay safe and secure!\n\nBest regards,\nThe My Gym Buddy Team"

        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, [email], fail_silently=False)
        print("Password change OTP email sent successfully!")

    except BadHeaderError as e:
        print(f"Error sending email: {e}")
    except CustomUser.DoesNotExist as e:
        print(f"Error updating user object: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

