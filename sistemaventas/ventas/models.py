from django.db import models
from django.forms import model_to_dict

# Create your models here.

class Clientes(models.Model):
    nif = models.CharField(max_length=200, unique=True, null= True, blank=True)
    codigo = models.CharField(max_length=200, unique=True, null=True, blank=True)
    nombre = models.CharField(max_length=200, null=False, blank=False)
    apellido = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=200, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='cliente'
        verbose_name_plural ='clientes'
        # order_with_respect_to ='description'
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=200, null=True, unique=True, blank=True)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    # imagen = models.ImageField(upload_to='productos', null=True)
    costo = models.DecimalField(max_length=10,null=True,default=0,decimal_places=2, max_digits=10, blank=True)
    precio = models.DecimalField(max_length=10, null=True,  decimal_places=2, max_digits=10, blank=True)
    cantidad = models.DecimalField(max_length=200, null=True ,decimal_places=2,  max_digits=10, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural ='productos'
        # order_with_respect_to ='descripcion'
    
    def __str__(self):
        return self.nombre

##########################################################################

class Egreso(models.Model):
    fecha_pedido = models.DateField(max_length=255)
    cliente = models.ForeignKey(Clientes, on_delete=models.SET_NULL , null=True , related_name='cliente')
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    pagado = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    comentarios = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    ticket = models.BooleanField(default=True)
    desglosar = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=True , null=True)

    class Meta:
        verbose_name='egreso'
        verbose_name_plural = 'egresos'
        order_with_respect_to = 'fecha_pedido'
    
    def __str__(self):
        return str(self.id)
   

class ProductosEgreso(models.Model):
    egreso = models.ForeignKey(Egreso, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=20, decimal_places=2 , null=False)
    precio = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    subtotal = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    iva = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    total = models.DecimalField(max_digits=20, decimal_places=2 , null=False , default=0)
    created = models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=True)
    devolucion = models.BooleanField(default=False)

    class Meta:
        verbose_name='producto egreso'
        verbose_name_plural = 'productos egreso'
        order_with_respect_to = 'created'
    
    def __str__(self):
        return self.producto
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['created'])
        return item


####################################################################################

class Empresa(models.Model):
    rnc = models.CharField(max_length=200, unique=True, null= True, blank=True)
    nombre = models.CharField(max_length=200, null=False, blank=False)
    # imagen = models.ImageField(upload_to='empresa', null=True)
    domicilio = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=200, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='empresa'
        verbose_name_plural ='empresas'
        # order_with_respect_to ='description'
    
    def __str__(self):
        return self.nombre