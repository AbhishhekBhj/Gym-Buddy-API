# Generated by Django 4.2.3 on 2024-02-23 07:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exercise', '0002_exercise_calories_burned_per_hour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('routine_id', models.AutoField(primary_key=True, serialize=False)),
                ('sets', models.IntegerField(default=1)),
                ('reps', models.IntegerField(default=1)),
                ('weight', models.IntegerField(default=1)),
                ('notes', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('exericse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='CustomRoutine',
            fields=[
                ('custom_routine_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('routine', models.ManyToManyField(to='customroutine.routine')),
            ],
        ),
    ]