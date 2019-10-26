from django import forms
from .models import ClsCarrera

class FormCarrera(forms.ModelForm):
    class Meta:
        model = ClsCarrera
        fields = ['descripcion', 'grado', 'seccion',  'estado']
