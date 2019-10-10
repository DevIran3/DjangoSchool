from django.db import models
from Apps.AppUsuario.models import ClsUsuario
# Create your models here.

class ClsProfesor(models.Model):
    pk_profesor = models.AutoField(primary_key=True)
    dpi = models.CharField(max_length=20)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    fecha_ingreso = models.DateField()
    estado = models.IntegerField()
    fk_usuario = models.OneToOneField(ClsUsuario, null=False, blank=False, on_delete=models.CASCADE)