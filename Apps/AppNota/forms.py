from django import forms
from .models import ClsNota

class FormNota(forms.ModelForm):
    class Meta:
        model = ClsNota
        fields = ['parcial_1',
                  'parcial_2',
                  'zona',
                  'parcial_3',
                  'final',
                  'fecha_ingreso',
                  'fecha_modificacion',
                  'estado',
                  'fk_curso',
                  'fk_carrera',
                  'fk_profesor',
                  'fk_establecimiento',
                  'fk_alumno'
                  ]