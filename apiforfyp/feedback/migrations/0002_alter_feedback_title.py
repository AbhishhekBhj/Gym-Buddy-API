# Generated by Django 5.0.1 on 2024-04-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='title',
            field=models.CharField(max_length=2000),
        ),
    ]
