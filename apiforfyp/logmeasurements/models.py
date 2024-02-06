from django.db import models
from users.models import CustomUser
import uuid


class BodyMeasurement(models.Model):
    measurement_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    # Anthropometric measurements
    height = models.FloatField(help_text="Height in inches", default=0)
    weight = models.FloatField(help_text="Weight in kilograms", default=0)
    chest_size = models.FloatField(help_text="Chest size in inches", default=0)
    waist_size = models.FloatField(help_text="Waist size in inches", default=0)
    hip_size = models.FloatField(help_text="Hip size in inches", default=0)

    # Limb measurements
    left_arm = models.FloatField(help_text="Left arm size in inches", default=0)
    right_arm = models.FloatField(help_text="Right arm size in inches", default=0)

    left_quadricep = models.FloatField(
        help_text="Left quadricep size in inches", default=0
    )
    right_quadricep = models.FloatField(
        help_text="Right quadricep size in inches", default=0
    )
    left_calf = models.FloatField(help_text="Left calf size in inches", default=0)
    right_calf = models.FloatField(help_text="Right calf size in inches", default=0)
    left_forearm = models.FloatField(help_text="Left forearm size in inches", default=0)
    right_forearm = models.FloatField(
        help_text="Right forearm size in inches", default=0
    )
    # Additional information
    notes = models.TextField(
        blank=True, null=True, help_text="Additional notes or comments", default=""
    )

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Body measurement for {self.user} on {self.created_at}"
