from django.urls import path
from . import views


urlpatterns = [
    # path('create/', views.CustomUserCreate.as_view(), name='account-create'),
    path('users/', views.CustomUserView.as_view()),
    path('users1/', views.CustomUserViewSet.as_view()),

]


