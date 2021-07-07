from django.contrib import admin
from .models import Categoria, Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria', 'precio']
    search_fields = ["titulo",]
    list_filter = ["titulo", "categoria"]
    list_per_page = 5

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
