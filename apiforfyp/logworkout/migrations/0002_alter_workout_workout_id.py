# Generated by Django 4.2.3 on 2024-01-28 06:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('logworkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='workout_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]