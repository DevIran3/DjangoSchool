from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import FormEstablecimiento
from .models import ClsEstablecimiento

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
        return render(request, 'TempEstablecimiento/InsertEstablecimiento.html', {'EstablecimientoForm': EstablecimientoForm})



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
                return redirect('index')
    except ObjectDoesNotExist as e:
        Error = e
    return render(request, 'TempEstablecimiento/InsertEstablecimiento.html', {'EstablecimientoForm':EstablecimientoForm, 'Error':Error})



def DeleteEstablecimiento(request, pk_establecimiento):
    clsEstablecimiento = ClsEstablecimiento.objects.get(pk_establecimiento = pk_establecimiento)
    if request.method == 'POST':
#Este metodo elimina directamente a la DB
#        clsEstablecimiento.delete()
        clsEstablecimiento.estado = 0
        clsEstablecimiento.save()
        return redirect('index')
    return render(request, 'TempEstablecimiento/DeleteEstablecimiento.html', {'clsEstablecimiento':clsEstablecimiento})
