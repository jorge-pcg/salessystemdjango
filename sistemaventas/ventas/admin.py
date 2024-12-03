from django.contrib import admin
from ventas.models import Clientes, Producto, Empresa

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre','nif', 'telefono', 'codigo')
    search_fields = ['nombre', 'nif']
    readonly_fields = ('date_created', 'date_update')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Clientes, ClientesAdmin)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'descripcion', 'cantidad')
    search_fields = ['nombre', 'codigo']
    readonly_fields = ('date_created', 'date_update')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Producto, ProductoAdmin)

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('rnc', 'nombre', 'telefono', 'domicilio')
    search_fields = ['nombre', 'rnc']
    readonly_fields = ('date_created', 'date_update')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Empresa, EmpresaAdmin)

