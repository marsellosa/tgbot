from django.db import models

class Categoria(models.Model):

    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.IntegerField(default=1)
    puntos_volumen = models.FloatField(max_length=10)
    distribuidor = models.FloatField(max_length=10)
    consultor_mayor = models.FloatField(max_length=10)
    productor_calificado = models.FloatField(max_length=10)
    mayorista = models.FloatField(max_length=10)
    cliente_bs = models.FloatField(max_length=10)
    cliente_sus = models.FloatField(max_length=10)
    pais = models.ForeignKey('Pais', on_delete=models.SET_NULL, null=True, blank=True)
    activo = models.BooleanField(default=True)
    inserted_on = models.DateField(auto_now_add=True)
    edited_on = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "Productos Cerrados"

    def __str__(self):
        return self.nombre

class Sabor(models.Model):

    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)
    sabor = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Sabores'

    def __str__(self):
        return self.sabor
    
class Pais(models.Model):

    nombre = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.nombre

class Detalles(models.Model):

    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)
    sku = models.CharField(max_length=8)
    detalles = models.CharField(max_length=255, blank=True, null=True)
    codigo_barras = models.CharField(max_length=16, blank=True, null=True)
    activo = models.BooleanField(default=True)
    
    class Meta:
        managed = True
        verbose_name = 'Detalle:'
        verbose_name_plural = 'Detalles:'

    def __str__(self):
        return self.sku
    