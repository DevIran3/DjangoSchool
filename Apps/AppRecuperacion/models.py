from django.db import models
from Apps.AppCurso.models import ClsCurso
from Apps.AppCarrera.models import ClsCarrera
from Apps.AppProfesor.models import ClsProfesor
from Apps.AppEstablecimiento.models import ClsEstablecimiento
from Apps.AppAlumno.models import ClsAlumno

# Create your models here.

class ClsRecuperacion(models.Model):
    pk_recuperacion = models.AutoField(primary_key=True)
    final = models.IntegerField()
    fecha_ingreso = models.DateField()
    fecha_modificacion = models.DateField()
    estado = models.IntegerField(default=1)
    fk_curso = models.ForeignKey(ClsCurso, null=False, blank=False, on_delete=models.CASCADE)
    fk_carrera = models.ForeignKey(ClsCarrera, null=False, blank=False, on_delete=models.CASCADE)
    fk_profesor = models.ForeignKey(ClsProfesor, null=False, blank=False, on_delete=models.CASCADE)
    fk_establecimiento = models.ForeignKey(ClsEstablecimiento, null=False, blank=False, on_delete=models.CASCADE)
    fk_alumno = models.ForeignKey(ClsAlumno, null=False, blank=False, on_delete=models.CASCADE)


