from django.shortcuts import render
from easy_pdf.views import PDFTemplateView
from .models import *
from usuarios.models import Empleado
from django.shortcuts import redirect
from datetime import date
# Create your views here.


class FichadeProductos(PDFTemplateView):
    # se crea la clase de Ficha de Producto
    # para poder generar informe de Productos Vencidos
    template_name = "InformedeProductos.html"

    def get_context_data(self, **kwargs):
        # la variable prods recoge todos los detalles existentes
        prods = DetalleProducto.objects.all()
        day = date.today()
        # la variable day captura la fecha de hoy
        return super(FichadeProductos, self).get_context_data(
            pagesize="Letter",
            title="Productos",
            prods=prods,
            # de manda la variable prods que es en la que están todos
            # los detalles de productos al template
            day=day,
            # se manda la variable day con la fecha de hoy al template
            **kwargs
            )


class FichadeProductosproximos(PDFTemplateView):
    # se crea la clase de Ficha Productos Proximo
    # el cual es el que visualiza los productos
    # a punto de vencer
    template_name = "InformedeProductosproximos.html"

    def get_context_data(self, **kwargs):
        prods = DetalleProducto.objects.exclude(fechavencimiento=None)
        # Se crea la variable prods que manda a capturar todos los
        # detalles de productos excluyendo todos aquellos que no tengan
        # fecha de Vencimiento
        producto = Producto.objects.all()
        # la variable producto manda a capturar todos los productos que existen
        day = date.today()
        # captura la fecha de hoy
        return super(FichadeProductosproximos, self).get_context_data(
            pagesize="Letter",
            title="Productos",
            # se mandan los atributos prods, producto y day al template
            prods=prods,
            producto=producto,
            day=day,
            **kwargs
            )


class FichadeProductosOrden(PDFTemplateView):
    # se crea la ficha para impresion de informe de
    # productos que estan en orden
    template_name = "InformedeProductosenOrden.html"

    def get_context_data(self, **kwargs):
        prods = DetalleProducto.objects.all()
        # prods manda a capturar todos los detalles de productos
        producto = Producto.objects.all()
        # producto manda a capturar todos los productos
        day = date.today()
        return super(FichadeProductosOrden, self).get_context_data(
            pagesize="Letter",
            title="Productos",
            # se mandan al template de productos en orden las variables
            # prods, producto y day
            prods=prods,
            producto=producto,
            day=day,
            **kwargs
            )
