from django.urls import path
from .views import patient_list

urlpatterns = [
    path('test/', patient_list, name='patient_list')
]
