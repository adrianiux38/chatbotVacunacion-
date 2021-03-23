from django.db import models

# Create your models here.

class RegistrosVacunacion(models.Model):
    sender = models.CharField(primary_key=True, max_length=13)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    cp = models.CharField(max_length=5, blank=True, null=True)
    edad = models.CharField(max_length=10, blank=True, null=True)
    delegacion = models.TextField(blank=True, null=True)
    pertenece_medico = models.CharField(max_length=2, blank=True, null=True)
    partido_apoyado = models.CharField(max_length=2, blank=True, null=True)
    apoya_morena = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registros_vacunacion'