from django.urls import path
from . import views

urlpatterns = [
        path('carrito/', views.carrito, name='carrito'),
        path('agregar/<producto_id>/', views.agregar_producto, name='agregar_producto'),
        path('eliminar/<producto_id>/', views.eliminar_producto, name='eliminar_producto'),
        path('restar/<producto_id>/', views.restar_producto, name='restar_producto'),
        path('vaciar/', views.vaciar_carrito, name='vaciar_carrito'),
        path('pronto/', views.pronto, name='pronto'),
    ]
