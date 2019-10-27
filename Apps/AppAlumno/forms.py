from django import forms
from .models import ClsAlumno

class FormAlumno(forms.ModelForm):
    class Meta:
        model = ClsAlumno
        fields = ['nombre', 'apellido', 'fecha_ingreso', 'contacto', 'email', 'direccion', 'estado', 'fk_carrera', 'fk_usuario']