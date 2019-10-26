from django.db import models

# Create your models here.

class ClsCarrera(models.Model):
#   id = PrimaryKey
    descripcion = models.CharField(max_length=50)
    grado = models.CharField(max_length=5)
    seccion = models.CharField(max_length=5)
    estado = models.IntegerField()