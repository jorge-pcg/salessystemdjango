from django import forms
from ventas.models import Clientes, Producto, ProductosEgreso

class ClienteForm(forms.ModelForm):
    class Meta:
        imagen = forms.ImageField()
        model = Clientes
        fields = ('codigo', 'nombre', 'apellido', 'telefono', 'direccion','nif')
        labels = {
            'codigo': 'Código: ',
            'nombre': 'Nombre: ',
            'apellido': 'Email: ',
            'telefono': 'Telefono: ',
            'direccion': 'Direccion: ',
            'nif': 'NIF: ',
        }

class AddClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ('codigo', 'nombre', 'apellido', 'telefono', 'direccion','nif')
        labels = {
            'codigo': 'Código: ',
            'nombre': 'Nombre: ',
            'apellido': 'Email: ',
            'telefono': 'Telefono: ',
            'direccion': 'Direccion: ',
            'nif': 'NIF: ',
        }

class EditarClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        # fields = ('codigo', 'nombre', 'apellido', 'telefono','nif')
        fields = ('codigo', 'nombre', 'apellido', 'telefono', 'direccion','nif')
        labels = {
            'codigo': 'Código: ',
            'nombre': 'Nombre: ',
            'apellido': 'Email: ',
            'telefono': 'Telefono: ',
            'direccion': 'Direccion: ',
            'nif': 'NIF: ',
        }

        widgets = {
            'codigo': forms.TextInput(attrs={'type': 'text', 'id': 'codigo_editar'}),
            'nombre': forms.TextInput(attrs={'id': 'nombre_editar'}),
            'apellido': forms.TextInput(attrs={'id': 'apellido_editar'}),
            'telefono': forms.TextInput(attrs={'id': 'telefono_editar'}),
            'direccion': forms.TextInput(attrs={'id': 'direccion_editar'}),
            'nif': forms.TextInput(attrs={'id': 'nif_editar'}),
        }

#######################################################################################################
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo', 'nombre', 'descripcion', 'costo', 'precio', 'cantidad')
        labels = {
            'codigo': 'Código Producto: ',
            'nombre': 'Nombre: ',
            'descripcion': 'Descripcion: ',
            # 'imagen': 'Imagen: ',
            'costo': 'Costo: ',
            'precio': 'Precio: ',
            'cantidad': 'Cantidad: ',
        }

class AddProductoForm(forms.ModelForm):
    class Meta:
        imagen = forms.ImageField()
        model = Producto
        fields = ('codigo', 'nombre', 'descripcion', 'costo', 'precio', 'cantidad')
        labels = {
            'codigo': 'Código Producto: ',
            'nombre': 'Nombre: ',
            'descripcion': 'Descripcion: ',
            # 'imagen': 'Imagen: ',
            'costo': 'Costo: ',
            'precio': 'Precio: ',
            'cantidad': 'Cantidad: ',
        }

class EditarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        # imagen = forms.ImageField()
        fields = ('codigo', 'nombre', 'descripcion', 'costo', 'precio', 'cantidad')
        labels = {
            'codigo': 'Código Producto: ',
            'nombre': 'Nombre: ',
            'descripcion': 'Descripcion: ',
            # 'imagen': 'Imagen: ',
            'costo': 'Costo: ',
            'precio': 'Precio: ',
            'cantidad': 'Cantidad: ',
        }

        widgets = {
            'codigo': forms.TextInput(attrs={'type': 'text', 'id': 'codigo_editar'}),
            'nombre': forms.TextInput(attrs={'id': 'nombre_editar'}),
            'descripcion': forms.TextInput(attrs={'id': 'descripcion_editar'}),
            'costo': forms.TextInput(attrs={'id': 'costo_editar'}),
            'precio': forms.TextInput(attrs={'id': 'precio_editar'}),
            'cantidad': forms.TextInput(attrs={'id': 'cantidad_editar'}),
        }

###########################################################################################################

class EditarProductoEgresoForm(forms.ModelForm):
    class Meta:
        model = ProductosEgreso
        # imagen = forms.ImageField()
        fields = ('egreso', 'producto', 'cantidad', 'precio', 'subtotal', 'cantidad')
        labels = {
            'codigo': 'Código Producto: ',
            'nombre': 'Nombre: ',
            'descripcion': 'Descripcion: ',
            # 'imagen': 'Imagen: ',
            'costo': 'Costo: ',
            'precio': 'Precio: ',
            'cantidad': 'Cantidad: ',
        }

        widgets = {
            'codigo': forms.TextInput(attrs={'type': 'text', 'id': 'codigo_editar'}),
            'nombre': forms.TextInput(attrs={'id': 'nombre_editar'}),
            'descripcion': forms.TextInput(attrs={'id': 'descripcion_editar'}),
            'costo': forms.TextInput(attrs={'id': 'costo_editar'}),
            'precio': forms.TextInput(attrs={'id': 'precio_editar'}),
            'cantidad': forms.TextInput(attrs={'id': 'cantidad_editar'}),
        }