from rest_framework import serializers
from .models import CustomUser
from .models import Package


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'bio')