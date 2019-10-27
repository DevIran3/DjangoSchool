from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import ClsAdministrativo
from Apps.AppUsuario.models import ClsUsuario
from .forms import FormAdministrativo

# Create your views here.


def Home(request):
    return render(request, 'TempAdministrativo/index.html')

def SelectAdministrativo(request):
    clsAdministrativo = ClsAdministrativo.objects.filter(estado = 1)
    return render(request, 'TempAdministrativo/SelectAdministrativo.html', {'clsAdministrativo': clsAdministrativo})

def InsertAdministrativo(request):
    if request.method == 'POST':
        _nombre = request.POST.get('nombre')
        _apellido = request.POST.get('apellido')
        _dpi = request.POST.get('dpi')
        _fecha_ingreso = request.POST.get('fecha_ingreso')
        _estado = request.POST.get('estado')
        _fk_usuario = request.POST.get('fk_usuario')
        clsAdministrativo = ClsAdministrativo(nombre = _nombre,
                              apellido = _apellido,
                              dpi = _dpi,
                              fecha_ingreso = _fecha_ingreso,
                              estado = _estado,
                              fk_usuario = ClsUsuario.objects.get(pk_usuario = _fk_usuario))
        clsAdministrativo.save()
        return redirect('http://127.0.0.1:8000/Administrativo/Inicio/')
    return render(request, 'TempAdministrativo/InsertAdministrativo.html')

def UpdateAdministrativo(request, pk_administrativo):
    Error = None
    formAdministrativo = None
    try:
        clsAdministrativo = ClsAdministrativo.objects.get(pk_administrativo = pk_administrativo)
        if request.method == 'GET':
            formAdministrativo = FormAdministrativo(instance = clsAdministrativo)
        else:
            formAdministrativo = FormAdministrativo(request.POST, instance = clsAdministrativo)
            if formAdministrativo.is_valid():
                formAdministrativo.save()
                return redirect('http://127.0.0.1:8000/Administrativo/Inicio/')
    except ObjectDoesNotExist as e:
        Error = e
    return render(request, 'TempAdministrativo/InsertAdministrativo.html', {'formAdministrativo':formAdministrativo, 'Error':Error, 'clsAdministrativo':clsAdministrativo})

def FindUpdateAdministrativo(request):
    if request.method == 'GET':
        return render(request, 'TempAdministrativo/FindAdministrativo.html')
    if request.method == 'POST':
        return redirect('UpdateAdministrativo', request.POST.get('pk_administrativo'))

def DeleteAdministrativo(request, pk_administrativo):
    Error = None
    clsAdministrativo = None
    try:
        clsAdministrativo = ClsAdministrativo.objects.get(pk_administrativo = pk_administrativo)
        if request.method == 'POST':
#   Este metodo elimina directamente a la DB
#   clsEstablecimiento.delete()
            clsAdministrativo.estado = 0
            clsAdministrativo.save()
            return redirect('http://127.0.0.1:8000/Administrativo/Inicio/')
    except Exception as e:
        Error = "No se encontro ningun registro con ", pk_administrativo
    return render(request, 'TempAdministrativo/DeleteAdministrativo.html', {'clsAdministrativo':clsAdministrativo, 'Error':Error})

def FindDeleteAdministrativo(request):
    if request.method == 'GET':
        return render(request, 'TempAdministrativo/FindAdministrativo.html')
    if request.method == 'POST':
        return redirect('DeleteAdministrativo', request.POST.get('pk_administrativo'))
