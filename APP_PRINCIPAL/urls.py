from django.urls import path
from . import views

urlpatterns = [
        path('', views.principal, name='principal'),
        path('acerca/', views.acerca_de, name='acerca_de'),
    ]
