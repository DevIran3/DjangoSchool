from django import forms
from .models import ClsUsuario

class FormUsuario(forms.ModelForm):
    class Meta:
        model = ClsUsuario
        fields = ['codigo_usuario', 'contrasena', 'estado', 'fk_school']