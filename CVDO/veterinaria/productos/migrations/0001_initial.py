# Generated by Django 2.2.4 on 2019-08-27 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Ingrese Imagen')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('porcentaje', models.PositiveIntegerField(blank=True, null=True, verbose_name='Porcentaje')),
                ('existencia', models.PositiveIntegerField(default=0, verbose_name='existencia')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'Producto',
            },
        ),
        migrations.CreateModel(
            name='ubicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacionproducto', models.CharField(default='Estante 1', max_length=150, null=True, verbose_name='Ubicacion del Producto')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroloteproducto', models.CharField(max_length=150, null=True, verbose_name='Numero de lote del Producto')),
                ('cantidad', models.PositiveIntegerField(default=0, null=True, verbose_name='Cantidad')),
                ('preciocompra', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Precio Costo')),
                ('precioventa', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Precio Venta')),
                ('fechavencimiento', models.DateField(verbose_name='Fecha de Vencimiento')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='elproducto', to='productos.Producto')),
                ('ubicacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.ubicacion')),
            ],
            options={
                'verbose_name': 'DetalleProducto',
                'verbose_name_plural': 'DetallesdeProductos',
                'db_table': 'DetalleProducto',
            },
        ),
    ]
