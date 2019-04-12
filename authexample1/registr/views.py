from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import viewsets


class CustomUserView(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response({"users": serializer.data})

    # def post(self, request):
    #     user = request.data.get('user')
    #     serializer = CustomUserSerializer(data=user)
    #     if serializer.is_valid(raise_exception=True):
    #         saved_user = serializer.save()
    #     return Response({"success": "User {} created successfully".format(saved_user.username)})


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer