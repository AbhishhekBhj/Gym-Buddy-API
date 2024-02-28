from users.email import send_dummy_mail


def send_motivating_mails():
    send_dummy_mail(
        email="abhujel322@gmail.com",
        message="You are doing great! Keep it up!",
        subject="Motivation",
    )
