from rest_framework import serializers
from .models import Todo
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "is_superuser",
            "is_staff",
            "password",
        )

class TodoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Todo
        fields = "__all__"
        