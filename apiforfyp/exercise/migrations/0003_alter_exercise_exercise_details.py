# Generated by Django 5.0.1 on 2024-01-21 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0002_alter_targetbodypart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='exercise_details',
            field=models.TextField(),
        ),
    ]
