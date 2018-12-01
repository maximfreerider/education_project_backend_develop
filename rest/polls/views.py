from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.request import Request

from polls.serializers import UserSerializer
from polls.models import User
from rest_framework.views import APIView


class Users(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({serializer.data})