from django.urls import path
from .views import post_list

urlpatterns = [
    path('test/', post_list, name='post_list')
]
