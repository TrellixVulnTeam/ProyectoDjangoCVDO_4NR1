# Generated by Django 2.1.7 on 2019-10-03 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0009_detalleproducto_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleproducto',
            name='estado',
            field=models.BooleanField(editable=False, verbose_name='Estado'),
        ),
    ]
