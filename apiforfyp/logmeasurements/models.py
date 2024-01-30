from django.db import models
from users.models import CustomUser
import uuid

class BodyMeasurement(models.Model):
    measurement_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    # Anthropometric measurements
    height = models.FloatField(help_text="Height in centimeters")
    weight = models.FloatField(help_text="Weight in kilograms")
    chest_size = models.FloatField(help_text="Chest size in centimeters")
    waist_size = models.FloatField(help_text="Waist size in centimeters")
    hip_size = models.FloatField(help_text="Hip size in centimeters")
    
    # Limb measurements
    left_arm = models.FloatField(help_text="Left arm size in centimeters")
    right_arm = models.FloatField(help_text="Right arm size in centimeters")
    left_leg = models.FloatField(help_text="Left leg size in centimeters")
    right_leg = models.FloatField(help_text="Right leg size in centimeters")
    
    # Additional information
    notes = models.TextField(blank=True, null=True, help_text="Additional notes or comments")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Body measurement for {self.user} on {self.created_at}"
