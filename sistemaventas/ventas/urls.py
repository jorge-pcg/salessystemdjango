from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ventas_view, name='Ventas'),
    path('clientes/', views.clientes_view, name='Clientes'),
    path('add_clientes/', views.add_clientes_view, name='AddCliente'),
    path('edit_clientes/', views.edit_clientes_view, name='EditCliente'),
    path('delete_clientes/', views.delete_clientes_view, name='DeleteCliente'),
    path('productos/', views.productos_view, name='Productos'),
    path('add_productos/', views.add_producto_view, name='AddProducto'),
    path('edit_producto/', views.edit_producto_view, name='EditProducto'),
    path('delete_producto/', views.delete_producto_view, name='DeleteProducto'),
    path('add_venta/',views.add_ventas.as_view(), name='AddVenta'),
    path('delete_venta/', views.delete_venta_view, name='DeleteVenta'),
    path('export/', views.export_pdf_view, name="ExportPDF" ),
    path('export/<id>/<iva>', views.export_pdf_view, name="ExportPDF" ),
]
