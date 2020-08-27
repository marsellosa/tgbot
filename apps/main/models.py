from django.db import models


class Settings(models.Model):

    nombre = models.CharField("Nombre", max_length=50)
    descripcion = models.CharField(
        "Descripcion", max_length=100, blank=True, null=True)
    valor = models.CharField("Valor", max_length=50)

    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"

    def __str__(self):
        return self.valor
