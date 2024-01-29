from django.db import models

from users.models import CustomUser
import uuid


class Reminder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Reminder set by {self.user} on {self.created_at}"
