from django import forms
from .models import ClsAdministrativo

class FormAdministrativo(forms.ModelForm):
    class Meta:
        model = ClsAdministrativo
        fields = ['nombre', 'apellido', 'dpi', 'fecha_ingreso', 'estado', 'fk_usuario']
