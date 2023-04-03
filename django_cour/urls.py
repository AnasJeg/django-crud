from django.contrib import admin
from django.urls import path,include
from cours import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cours.urls')),
    path('',views.patient_list,name="index"),
    path('add',views.add,name="add"),
    path("update/<int:id>",views.update,name="update"),
    path("delete/<int:id>",views.delete,name="delete")
]
