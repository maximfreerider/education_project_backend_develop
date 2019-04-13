from django.urls import path, include
from . import views


urlpatterns = [
    # path('create/', views.CustomUserCreate.as_view(), name='account-create'),
    # path('users/', views.CustomUserView.as_view()),
    path('generics/users/', views.CustomUserListView.as_view()),
    path('generics/users/<int:id>/', views.CustomUserListView.as_view()),
]


