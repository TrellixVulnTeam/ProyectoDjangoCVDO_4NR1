# Generated by Django 2.2.4 on 2019-09-21 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('ventas', '0002_detalleventa_numeroloteproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprobanteventa',
            name='vendedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='usuarios.Empleado'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comprobanteventa',
            name='total',
            field=models.FloatField(default=0.0, null=True, verbose_name='Total'),
        ),
    ]
