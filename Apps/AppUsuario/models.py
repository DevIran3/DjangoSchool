from django.db import models

from Apps.AppEstablecimiento.models import ClsEstablecimiento

# Create your models here.

class ClsUsuario(models.Model):
    pk_usuario = models.AutoField(primary_key=True)
    codigo_usuario = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50, unique=True)
    contrasena = models.CharField(max_length=12)
    estado = models.IntegerField()
    fk_school = models.ForeignKey(ClsEstablecimiento, null=False, blank=False, on_delete=models.CASCADE)