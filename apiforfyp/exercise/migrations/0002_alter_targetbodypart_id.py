# Generated by Django 5.0.1 on 2024-01-21 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='targetbodypart',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]