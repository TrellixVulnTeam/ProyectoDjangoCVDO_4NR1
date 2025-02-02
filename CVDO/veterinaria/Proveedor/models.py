from django.db import models

# Create your models here.


class Proveedor(models.Model):
    nit = models.CharField('NIT', max_length=11, unique=True)
    nombre = models.CharField('Nombre', max_length=80)
    direccion = models.CharField('Direccion', max_length=150)
    telefono = models.CharField('Telefono', max_length=15)

    def __str__(self):
        return "%s  %s" % (self.nombre, self.direccion)

    class Meta:
        db_table = 'Proveedor'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
