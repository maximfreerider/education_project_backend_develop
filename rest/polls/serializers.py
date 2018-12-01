from rest_framework import serializers
from polls.models import User


class UserSerializer(serializers.ModelSerializer):
    """ Сериализация пользователей"""

    class Meta:
        model = User
        fields = ('first_name', 'surname', 'email')