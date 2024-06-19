# Generated by Django 5.0.6 on 2024-06-03 11:45

from django.db import migrations, models
import datetime

def set_default_completed_at(apps, schema_editor):
    Todo = apps.get_model('todo', 'Todo')
    todos = Todo.objects.filter(completed_at__isnull=True)
    for todo in todos:
        todo.completed_at = datetime.datetime.now()
        todo.save()

class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0004_remove_todo_star_alter_todo_completed_at"),
    ]

    operations = [
        migrations.RunPython(set_default_completed_at),
        migrations.AlterField(
            model_name="todo",
            name="completed_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
