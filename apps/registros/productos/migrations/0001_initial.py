# Generated by Django 2.2.13 on 2020-07-04 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('cantidad', models.IntegerField(default=1)),
                ('puntos_volumen', models.FloatField(max_length=10)),
                ('distribuidor', models.FloatField(max_length=10)),
                ('consultor_mayor', models.FloatField(max_length=10)),
                ('productor_calificado', models.FloatField(max_length=10)),
                ('mayorista', models.FloatField(max_length=10)),
                ('cliente_bs', models.FloatField(max_length=10)),
                ('cliente_sus', models.FloatField(max_length=10)),
                ('activo', models.BooleanField(default=True)),
                ('inserted_on', models.DateField(auto_now_add=True)),
                ('edited_on', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Productos Cerrados',
            },
        ),
    ]
