from django import forms
from .models import ClsRecuperacion

class FormRecuperacion(forms.ModelForm):
    class Meta:
        model = ClsRecuperacion
        fields = ['final',
                  'fecha_ingreso',
                  'fecha_modificacion',
                  'estado',
                  'fk_curso',
                  'fk_carrera',
                  'fk_profesor',
                  'fk_establecimiento',
                  'fk_alumno'
                  ]