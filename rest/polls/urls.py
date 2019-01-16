from django.urls import path
from polls.views import *


urlpatterns = [
    path('packages/', Packages.as_view()),
    path('users/', Users.as_view())
]