from django.db import models
from Apps.AppProfesor.models import ClsProfesor
from Apps.AppCarrera.models import ClsCarrera

# Create your models here.

class ClsCurso(models.Model):
    pk_curso = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()
    fk_profesor = models.ForeignKey(ClsProfesor, null=False, blank=False, on_delete=models.CASCADE)
    fk_carrera = models.ForeignKey(ClsCarrera, null=False, blank=False, on_delete=models.CASCADE)

