from django import forms
from .models import ClsCurso

class FormCurso(forms.ModelForm):
    class Meta:
        model = ClsCurso
        fields = ['descripcion', 'hora_entrada', 'hora_salida', 'fk_profesor', 'fk_carrera']