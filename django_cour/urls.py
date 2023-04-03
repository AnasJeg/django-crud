from django.contrib import admin
from django.urls import path,include
from cours import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cours.urls')),
    path('ajouter/',views.ajouter,name="ajouter")
]
