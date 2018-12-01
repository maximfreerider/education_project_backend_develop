from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.request import Request

from polls.serializers import PackageSerializer
from polls.models import User, Package
from rest_framework.views import APIView


# class Users(APIView):
#
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response({serializer.data})

class Packages(APIView):
    """ Всі пакети"""

    def get(self, request):
        packages = Package.objects.all()
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data)

    