# Generated by Django 2.1.7 on 2019-12-12 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0008_auto_20191212_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprobanteventa',
            name='pagado',
            field=models.BooleanField(default=True, verbose_name='Pagado'),
        ),
    ]
