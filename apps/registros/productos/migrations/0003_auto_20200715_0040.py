# Generated by Django 2.2.13 on 2020-07-15 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_categoria_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
