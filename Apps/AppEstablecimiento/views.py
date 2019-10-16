from django.shortcuts import render, redirect
from .forms import FormEstablecimiento

# Create your views here.
from requests import request


def Home(request):
    return render(request, 'TempEstablecimiento/index.html')

def InsertEstablecimiento(request):
    if request.method == 'POST':
        print(request.POST)
        Establecimiento = FormEstablecimiento(request.POST)
        if Establecimiento.is_valid():
            Establecimiento.save()
            return redirect('index')
    else:
        EstablecimientoForm = FormEstablecimiento()
        return  render(request, 'TempEstablecimiento/InsertEstablecimiento.html', {'EstablecimientoForm':EstablecimientoForm})