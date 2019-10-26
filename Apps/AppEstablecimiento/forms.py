from django import forms
from .models import ClsEstablecimiento

class FormEstablecimiento(forms.ModelForm):
    class Meta:
        model = ClsEstablecimiento
        fields = ['nombre', 'direccion', 'fundacion',  'estado']

