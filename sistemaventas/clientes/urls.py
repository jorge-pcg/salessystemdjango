from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.clientes_view , name='Clientes'),
]
