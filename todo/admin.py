from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "user",
        "id",
        "created_at",
        "updated_at",
        "completed_at",
    )