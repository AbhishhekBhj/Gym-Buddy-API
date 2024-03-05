from users.models import CustomUser
from django.core.mail import send_mail

from celery import task
from celery.utils.log import get_task_logger



logger = get_task_logger(__name__)


@task
def send_mail_to_all_users():
    users = CustomUser.objects.all()
    users_email =[]
    for user in users:
        users_email.append(user.email)
        
        