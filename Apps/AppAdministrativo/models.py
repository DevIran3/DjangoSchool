from django.db import models
from Apps.AppUsuario.models import ClsUsuario

# Create your models here.

class ClsAdministrativo(models.Model):
    pk_administrativo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    dpi = models.CharField(max_length=20)
    fecha_ingreso = models.DateField()
    estado = models.IntegerField()
    fk_usuario = models.OneToOneField(ClsUsuario, null=False, blank=False, on_delete=models.CASCADE)

