from django.core import serializers
from polls.models import User
from django.http import JsonResponse


def get_all_users(self):
    users = User.objects.all()
    data = serializers.serialize('json', users)
    return JsonResponse({'data': data})


