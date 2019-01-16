from django.urls import path
from registration import views

urlpatterns = [
    # path(r'^signup/$', core_views.signup, name='signup'),
    path('post_list/', views.post_list, name="post_list"),
    path('', views.show_info)
]