from django.db import models
from users.models import CustomUser


# Create your models here.


class FeedBack(models.Model):
    title = models.CharField(max_length=2000)
    feedback_provided_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    message = models.TextField()

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
