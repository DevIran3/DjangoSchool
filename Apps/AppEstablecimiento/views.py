from functools import partial
from tkinter.tix import _dummyFileComboBox

from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import FormEstablecimiento
from .models import ClsEstablecimiento

# Create your views here.
from requests import request

def HomeEstablecimiento(request):
    return render(request, 'TempEstablecimiento/index.html')

def InsertEstablecimiento(request):
    if request.method == 'POST':
        print(request.POST)
        _nombre = request.POST.get('nombre')
        _direccion = request.POST.get('direccion')
        _fundacion = request.POST.get('fundacion')
        _estado = request.POST.get('estado')
        print (_nombre, _direccion, _fundacion, _estado)
        clsEstablecimiento = ClsEstablecimiento(nombre = _nombre, direccion = _direccion, fundacion = _fundacion, estado = _estado)
        clsEstablecimiento.save()
        return redirect('HomeEstablecimiento')
    return render(request, 'TempEstablecimiento/InsertEstablecimiento.html')

def SelectEstablecimiento(request):
#    clsEstablecimientos = ClsEstablecimiento.objects.all()
    clsEstablecimientos = ClsEstablecimiento.objects.filter(estado = 1)
    return render(request, 'TempEstablecimiento/SelectEstablecimiento.html', {'clsEstablecimientos': clsEstablecimientos})

def UpdateEstablecimiento(request, pk_establecimiento):
    Error = None
    EstablecimientoForm = None
    try:
        clsEstablecimiento = ClsEstablecimiento.objects.get(pk_establecimiento = pk_establecimiento)
        if request.method == 'GET':
            EstablecimientoForm = FormEstablecimiento(instance = clsEstablecimiento)
        else:
            EstablecimientoForm = FormEstablecimiento(request.POST, instance=clsEstablecimiento)
            if EstablecimientoForm.is_valid():
                EstablecimientoForm.save()
                return redirect('HomeEstablecimiento')
    except ObjectDoesNotExist as e:
        Error = e
    return render(request, 'TempEstablecimiento/InsertEstablecimiento.html', {'EstablecimientoForm':EstablecimientoForm, 'Error':Error})

def DeleteEstablecimiento(request, pk_establecimiento):
    Error = None
    clsEstablecimiento = None
    try:
        clsEstablecimiento = ClsEstablecimiento.objects.get(pk_establecimiento=pk_establecimiento)
        if request.method == 'POST':
#Este metodo elimina directamente a la DB
#        clsEstablecimiento.delete()
            clsEstablecimiento.estado = 0
            clsEstablecimiento.save()
            return redirect('HomeEstablecimiento')
    except Exception as e:
        Error = "No se encontro ningun registro con ", pk_establecimiento
    return render(request, 'TempEstablecimiento/DeleteEstablecimiento.html', {'clsEstablecimiento':clsEstablecimiento, 'Error':Error})

def FindUpdateEstablecimiento(request):
    if request.method == 'GET':
        return render(request, 'TempEstablecimiento/FindEstablecimiento.html')
    if request.method == 'POST':
        return redirect('UpdateEstablecimiento', request.POST.get('pk_establecimiento'))

def FindDeleteEstablecimiento(request):
    if request.method == 'GET':
        return render(request, 'TempEstablecimiento/FindEstablecimiento.html')
    if request.method == 'POST':
        return redirect('DeleteEstablecimiento', request.POST.get('pk_establecimiento'))

