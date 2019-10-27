from django import forms
from .models import ClsProfesor

class FormProfesor(forms.ModelForm):
    class Meta:
        model = ClsProfesor
        fields = ['dpi', 'nombre', 'apellido', 'fecha_ingreso', 'estado', 'fk_usuario']