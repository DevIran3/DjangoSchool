from django.db import models
from Apps.AppCarrera.models import ClsCarrera
from Apps.AppUsuario.models import ClsUsuario

# Create your models here.

class ClsAlumno(models.Model):
    pk_alumno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    fecha_ingreso = models.DateField()
    contacto = models.CharField(max_length=8)
    email = models.EmailField(max_length=100)
    direccion = models.CharField(max_length=50)
    estado = models.IntegerField()
    fk_carrera = models.ForeignKey(ClsCarrera, null=False, blank=False, on_delete=models.CASCADE)
    fk_usuario = models.ForeignKey(ClsUsuario, null=False, blank=False, on_delete=models.CASCADE)
