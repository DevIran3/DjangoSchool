from django.db import models

# Create your models here.

class ClsEstablecimiento(models.Model):
    pk_establecimiento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=60)
    fundacion = models.DateField(max_length=50)
    estado = models.IntegerField()