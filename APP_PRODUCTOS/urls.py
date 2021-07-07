from django.urls import path
from . import views

urlpatterns = [
        path('agregar/', views.agregar, name='agregar'),
        path('visualizar/<id>/', views.visualizar, name='visualizar'),
        path('editar/<id>/', views.editar, name='editar'),
        path('borrar/<id>/', views.borrar, name='borrar'),
        path('categoria/<categoria_id>/', views.categoria, name='categoria'),
        path('buscar/', views.buscar, name='buscar'),
    ]

