# Generated by Django 5.0.6 on 2024-05-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="star",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
