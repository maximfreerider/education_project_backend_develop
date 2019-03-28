from polls.serializers import PackageSerializer
from polls.models import Package
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from polls.serializers import UserSerializer
from django.contrib.auth.models import User

class UserCreate(APIView):
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)


class UsersList(APIView):
    def get(self):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class PackagesList(APIView):
    """ Всі пакети"""
    def get(self, request):
        packages = Package.objects.all()
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data)

# class AuthRegister(generics.CreateAPIView):
#     permission_classes = (permissions.AllowAny)
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     # @transaction.atomic
#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





def index(request):
    return HttpResponse("Server is started")




