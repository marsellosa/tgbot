from django.db import models

class Categoria(models.Model):

    nombre = models.CharField(max_length=150, unique=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.IntegerField(default=1)
    puntos_volumen = models.FloatField(max_length=10)
    distribuidor = models.FloatField(max_length=10)
    consultor_mayor = models.FloatField(max_length=10)
    productor_calificado = models.FloatField(max_length=10)
    mayorista = models.FloatField(max_length=10)
    cliente_bs = models.FloatField(max_length=10)
    cliente_sus = models.FloatField(max_length=10)
    activo = models.BooleanField(default=True)
    inserted_on = models.DateField(auto_now_add=True)
    edited_on = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = "Productos Cerrados"

    def __str__(self):
        return self.nombre

