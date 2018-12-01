from django.urls import path
from polls.views import *
from . import views

urlpatterns = [
    path('users/', Users.as_view())
]