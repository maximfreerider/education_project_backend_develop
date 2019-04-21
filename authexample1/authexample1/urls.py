from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from registr.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registr.urls')),
    path('auth/login/', LoginView.as_view()),
    path('auth/logout/', LogoutView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    # path('api/v1/auth/', include('rest_framework.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

]
