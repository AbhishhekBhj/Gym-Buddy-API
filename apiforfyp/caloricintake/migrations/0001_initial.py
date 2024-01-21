# Generated by Django 4.2.3 on 2024-01-21 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CaloricIntake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories_consumed', models.FloatField(default=0.0)),
                ('serving_consumed', models.FloatField(default=0.0)),
                ('protein_consumed', models.FloatField(default=0.0)),
                ('carbs_consumed', models.FloatField(default=0.0)),
                ('fats_consumed', models.FloatField(default=0.0)),
                ('timestamp', models.DateTimeField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
