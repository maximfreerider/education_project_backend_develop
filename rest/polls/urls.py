from django.urls import path
from polls.views import *


urlpatterns = [
    path('package/', Packages.as_view())
]