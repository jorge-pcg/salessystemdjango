import json
from django.shortcuts import render, redirect
from .forms import AddClienteForm, EditarClienteForm, AddProductoForm, EditarProductoForm, ProductoForm
from django.contrib import messages
from .models import Clientes, Egreso, Producto, Egreso, ProductosEgreso, Empresa
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponse
from weasyprint.text.fonts import FontConfiguration
from django.template.loader import get_template
from weasyprint import HTML, CSS
from django.conf import settings
import os



# Create your views here.

def ventas_view(request):
    ventas = Egreso.objects.all()
    
    num_ventas = len(ventas)
    context = {
        'ventas': ventas,
        'num_ventas': num_ventas,
        'url': request._current_scheme_host
    }

    return render(request, 'ventas.html', context)

def clientes_view(request):
    clientes = Clientes.objects.all()
    form_personal = AddClienteForm()
    form_editar = EditarClienteForm()

    context = {
        'clientes': clientes,
        'form_personal': form_personal,
        'form_editar': form_editar,
    }
    return render(request, 'clientes.html', context)

def add_clientes_view(request):

    if request.POST:
        form = AddClienteForm(request.POST, request.FILES)

        if form.is_valid:
            try:
                form.save()
            except:
                messages(request, "Error al cargar cliente")
                return redirect('Clientes')
    return redirect('Clientes')

def edit_clientes_view(request):
    if request.POST:
        cliente = Clientes.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditarClienteForm(
            request.POST, request.FILES, instance= cliente)
        if form.is_valid:
            form.save()
    return redirect('Clientes')

def delete_clientes_view(request):
    if request.POST:
        cliente = Egreso.objects.get(pk=request.POST.get('id_personal_eliminar'))
        cliente.delete()
    return redirect('Clientes')

def delete_venta_view(request):
    if request.POST:
        egreso = Egreso.objects.get(pk=request.POST.get('id_producto_eliminar'))
        egreso.delete()
    return redirect('Ventas')

def productos_view(request):
    producto = Producto.objects.all()
    form_add = AddProductoForm()
    form_editar = EditarProductoForm()

    context = {
        'productos': producto,
        'form_add': form_add,
        'form_editar': form_editar,
    }
    return render(request, 'productos.html', context)

def add_producto_view(request):

    if request.POST:
        form = AddProductoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request, "Error al guardar productos")
                return redirect('Productos')
    return redirect('Productos')

def edit_producto_view(request):
    if request.POST:
        producto = Producto.objects.get(pk=request.POST.get('id_producto_editar'))

        # costo_a = request.POST['costo'].replace(',', '.')
        # request.POST['costo'] = costo_a
        
        
        form = EditarProductoForm(
            request.POST,  request.FILES, instance= producto
            )
        
        estado_mutable_anterior = request.POST._mutable
        request.POST._mutable = True
        if ',' in form.data['costo']:
            form.data['costo'] = form.data['costo'].replace(',', '.')

        if ',' in form.data['cantidad']:
            form.data['cantidad'] = form.data['cantidad'].replace(',', '.')
        
        if ',' in form.data['precio']:
            form.data['precio'] = form.data['precio'].replace(',', '.')

        # request.POST['precio'] = str(producto.precio)
        # request.POST['costo'] = str(producto.costo)
        # request.POST['cantidad'] = str(producto.cantidad)
        request.POST._mutable = estado_mutable_anterior

        if form.is_valid():
            form.save()
    return redirect('Productos')



def delete_producto_view(request):
    if request.POST:
        producto = Producto.objects.get(pk=request.POST.get('id_producto_eliminar'))
        producto.delete()
    return redirect('Productos')


class add_ventas(ListView):
    template_name = 'add_ventas.html'
    model = Egreso

    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    """
    def get_queryset(self):
        return ProductosPreventivo.objects.filter(
            preventivo=self.kwargs['id']
        )
    """
    def post(self, request,*ars, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'autocomplete':
                data = []
                for i in Producto.objects.filter(descripcion__icontains=request.POST["term"])[0:10]:
                    item = i.toJSON()
                    item['value'] = i.descripcion
                    data.append(item)
            elif action == 'save':
                total_pagado = float(request.POST["efectivo"]) + float(request.POST["tarjeta"]) + float(request.POST["transferencia"]) + float(request.POST["vales"]) + float(request.POST["otro"])
                fecha=request.POST["fecha"]
                id_cliente = int(request.POST["id_cliente"])
                cliente_obj = Clientes.objects.get(pk=id_cliente)
                datos = json.loads(request.POST["verts"])
                total_ventas = float(datos['total'])
                ticket_num = request.POST['ticket']

                if ticket_num == 1:
                    ticket = True
                else:
                    ticket = False

                desglosar_iva_num = int(request.POST["desglosar"])
                if desglosar_iva_num == 0:
                    desglosar_iva = False
                else:
                    desglosar_iva = True

                comentarios = request.POST["comentarios"]

                # Guardar ventas y productos
                nueva_venta = Egreso(
                    fecha_pedido = fecha, 
                    cliente= cliente_obj,
                    total = total_ventas,
                    pagado = total_pagado,
                    comentarios = comentarios,
                    ticket = ticket,
                    desglosar = desglosar_iva
                    )
                nueva_venta.save()

                # Guardar producto
                productos_egreso = []
                linea_pedido = datos['products']
                for i in linea_pedido:
                    producto_id = int(i['id'])
                    producto_obj = Producto.objects.get(pk=producto_id)
                    producto_cantidad = i['cantidad']
                    precio_formateado = i['precio'].replace(',','.')
                    producto_precio = float(precio_formateado)
                    iva=0
                    subtotal_formateado = i['subtotal'].replace(',','.')
                    producto_subtotal = float(subtotal_formateado)

                    producto_egreso = ProductosEgreso(
                        egreso = nueva_venta,
                        producto = producto_obj,
                        cantidad = producto_cantidad,
                        precio = producto_precio,
                        subtotal = producto_subtotal,
                        iva = iva,
                        total = iva + producto_subtotal
                        
                    )

                    producto_egreso.save()

            else:
                data['error'] = "Ha ocurrido un error"
                # return redirect('Productos')

            
        except Exception as e:
            data['error'] = str(e)
            # return redirect('Clientes')


        return JsonResponse(data,safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos_lista'] = Producto.objects.all()
        context['clientes_lista'] = Clientes.objects.all()

        return context


def export_pdf_view(request, id, iva):
    #print(id)
    template = get_template("ticket.html")
    #print(id)
    subtotal = 0 
    iva_suma = 0 

    venta = Egreso.objects.get(pk=float(id))
    datos = ProductosEgreso.objects.filter(egreso=venta)
    for i in datos:
        subtotal = subtotal + float(i.subtotal)
        iva_suma = iva_suma + float(i.iva)

    empresa = Empresa.objects.get(pk=1)
    context ={
        'num_ticket': id,
        'iva': iva,
        'fecha': venta.fecha_pedido,
        'cliente': venta.cliente,
        'items': datos, 
        'total': venta.total, 
        'empresa': empresa,
        'comentarios': venta.comentarios,
        'subtotal': subtotal,
        'iva_suma': iva_suma,
        # 'url': request._current_scheme_host
    }
    html_template = template.render(context)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"inline; filename=Cotizacion# {id}.pdf"
    css_url = os.path.join(settings.BASE_DIR,'ventas\static\index\css\\bootstrap.min.css')
    # HTML(string=html_template).write_pdf(target="ticket.pdf", stylesheets=[CSS(css_url)])
   
    font_config = FontConfiguration()
    HTML(string=html_template, base_url=request.build_absolute_uri()).write_pdf(target=response, font_config=font_config,stylesheets=[CSS(css_url)])

    return response
