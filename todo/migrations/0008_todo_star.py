# Generated by Django 5.0.6 on 2024-06-04 00:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0007_remove_todo_star"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="star",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
