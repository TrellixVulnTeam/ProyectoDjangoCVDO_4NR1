# Generated by Django 2.2.4 on 2019-09-17 05:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_auto_20190916_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_compra',
            name='FechaCompra',
            field=models.DateField(default=datetime.date(2019, 9, 16), verbose_name='FechaCompra'),
        ),
        migrations.AlterField(
            model_name='detalle_compra',
            name='numeroloteproducto',
            field=models.CharField(max_length=20, null=True, verbose_name='Numero de lote del Producto'),
        ),
    ]
