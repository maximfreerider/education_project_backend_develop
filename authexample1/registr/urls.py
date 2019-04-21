from django.urls import path, include
from . import views


urlpatterns = [
    # path('create/', views.CustomUserCreate.as_view(), name='account-create'),
    # path('users/', views.CustomUserView.as_view()),
    path('generics/users/', views.CustomUserListView.as_view()),
    path('generics/users/<int:id>/', views.CustomUserListView.as_view()),
    path('creating/acc/', views.CustomUserCreating.as_view()),
    path('accounts/', include('allauth.urls')),
    path('facebook/', views.FacebookLogin.as_view()),
]


