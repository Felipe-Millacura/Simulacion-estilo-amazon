# Generated by Django 2.1.2 on 2018-12-02 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carritoo', '0002_remove_producto_precioamazon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='PrecioFinal',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
