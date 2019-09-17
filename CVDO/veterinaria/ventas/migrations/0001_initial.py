# Generated by Django 2.2.4 on 2019-09-17 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('productos', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComprobanteVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha de Venta')),
                ('total', models.FloatField(default=0.0, verbose_name='Total')),
                ('efectivo', models.FloatField(default=0.0, null=True, verbose_name='Efectivo')),
                ('vuelto', models.FloatField(default=0.0, null=True, verbose_name='Vuelto')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
            ],
            options={
                'verbose_name': 'Comprobante de Venta',
                'verbose_name_plural': 'Comprobante de Ventas',
                'db_table': 'ComprobanteVenta',
            },
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pago', models.CharField(max_length=30, verbose_name='Tipo de Pago')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=0, verbose_name='Cantidad')),
                ('subtotal', models.FloatField(default=0, verbose_name='subtotal')),
                ('comprobante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eldetalle', to='ventas.ComprobanteVenta')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.Producto')),
            ],
            options={
                'verbose_name': 'Detalle de Venta',
                'verbose_name_plural': 'Detalle de Ventas',
                'db_table': 'DetalleVenta',
            },
        ),
        migrations.AddField(
            model_name='comprobanteventa',
            name='pago',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.TipoPago'),
        ),
    ]
