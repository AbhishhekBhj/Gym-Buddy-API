# Generated by Django 5.0.1 on 2024-04-20 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custommeal', '0002_remove_mealplan_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Snacks', 'Snacks')], max_length=20, unique=True)),
            ],
        ),
    ]
