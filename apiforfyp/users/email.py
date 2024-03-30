from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse
from .models import CustomUser
from random import randint
from .models import OTP



def send_forget_password_otp(email):
    try:
        # Generate OTP
        otp = randint(100000, 999999)

        # Compose email message
        subject = f"🔒 Password Reset OTP"
        message = f"Hello there!\n\nWe've received a request to reset your password. Your One-Time Password (OTP) for password reset is: {otp}.\n\nIf you didn't request this OTP, no worries - simply ignore this message.\n\nStay safe and secure!\n\nBest regards,\nThe My Gym Buddy Team"

        email_from = settings.EMAIL_HOST
        send_mail(subject, message, email_from, [email], fail_silently=False)

        OTP.objects.create(email=email, otp_code=otp)

        return otp
    
    except Exception as e:
        print(f"Error sending email or generating OTP: {e}")
        return None





def send_otp(email):
    try:
        # Generate OTP
        otp = randint(100000, 999999)

        # Compose email message
        subject = f"🎁 Special Delivery: Your Account Verification Code!"
        message = f"Hello there!\n\nWelcome to My Gym Buddy - your ultimate fitness companion! 🏋️‍♂️\n\nThank you for choosing us to help you on your fitness journey. Your One-Time Password (OTP) for account verification is: {otp}.\n\nWe're pumped to have you on board! Use this OTP to confirm your account and start sweating it out with our amazing features.\n\nIf you didn't request this OTP, no worries - simply ignore this message.\n\nStay motivated and keep pushing your limits!\n\nBest regards,\nThe My Gym Buddy Team"

        email_from = settings.EMAIL_HOST
        send_mail(subject, message, email_from, [email], fail_silently=False)

        OTP.objects.create(email=email, otp_code=otp)

        return otp

    except Exception as e:
        print(f"Error sending email or generating OTP: {e}")
        return None


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


def send_dummy_mail(email, subject, message):
    try:
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, [email], fail_silently=False)
        print("Dummy email sent successfully!")
    except BadHeaderError as e:
        print(f"Error sending email: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def send_special_offers(request, email):
    if request.method == "POST":
        subject = request.POST.get("subject", "Default Subject")
        message = request.POST.get("message", "Default Message")

        try:
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, [email], fail_silently=False)
            return HttpResponse("Special offers email sent successfully!")
        except BadHeaderError as e:
            # Log the error
            print(f"Error sending email: {e}")
            return HttpResponse(
                "Error sending email.", status=500
            )  # Internal Server Error
        except Exception as e:
            # Log the error
            print(f"An unexpected error occurred: {e}")
            return HttpResponse(
                "An unexpected error occurred.", status=500
            )  # Internal Server Error
    else:
        # Method Not Allowed for other request methods
        return HttpResponse("Method Not Allowed", status=405)  # Method Not Allowed


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


def send_mail_to_all_users(request):
    if request.method == "POST":
        subject = request.POST.get("subject", "Default Subject")
        message = request.POST.get("message", "Default Message")

        try:
            email_from = settings.EMAIL_HOST_USER
            all_users = CustomUser.objects.all()
            for user in all_users:
                send_mail(
                    subject,
                    message,
                    email_from,
                    [user.email],
                    fail_silently=False,
                )
            return HttpResponse("Email sent successfully to all users!")
        except BadHeaderError as e:
            # Log the error
            print(f"Error sending email: {e}")
            return HttpResponse(
                "Error sending email.", status=500
            )  # Internal Server Error
        except Exception as e:
            # Log the error
            print(f"An unexpected error occurred: {e}")
            return HttpResponse(
                "An unexpected error occurred.", status=500
            )  # Internal Server Error
    else:
        # Method Not Allowed for other request methods
        return HttpResponse("Method Not Allowed", status=405)  # Method Not Allowed
