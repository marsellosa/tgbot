# Generated by Django 2.2.14 on 2020-07-29 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0006_detalles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalles',
            old_name='detalle',
            new_name='detalles',
        ),
    ]
