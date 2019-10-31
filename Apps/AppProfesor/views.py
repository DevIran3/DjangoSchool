from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import ClsProfesor
from Apps.AppUsuario.models import ClsUsuario
from .forms import FormProfesor
# Create your views here.

def HomeProfesor(request):
    return render(request, 'TempProfesor/index.html')

def SelectProfesor(request):
    clsProfesor = ClsProfesor.objects.filter(estado = 1)
    return render(request, 'TempProfesor/SelectProfesor.html', {'clsProfesor': clsProfesor})

def InsertProfesor(request):
    if request.method == 'POST':
        _dpi = request.POST.get('dpi')
        _nombre = request.POST.get('nombre')
        _apellido = request.POST.get('apellido')
        _fecha_ingreso = request.POST.get('fecha_ingreso')
        _estado = request.POST.get('estado')
        _fk_usuario = request.POST.get('fk_usuario')
        clsProfesor = ClsProfesor(dpi = _dpi,
                                  nombre = _nombre,
                                  apellido = _apellido,
                                  fecha_ingreso = _fecha_ingreso,
                                  estado = _estado,
                                  fk_usuario = ClsUsuario.objects.get(pk_usuario = _fk_usuario))
        clsProfesor.save()
        return redirect('HomeProfesor')
    return render(request, 'TempProfesor/InsertProfesor.html')

def UpdateProfesor(request, pk_profesor):
    Error = None
    formProfesor = None
    try:
        clsProfesor = ClsProfesor.objects.get(pk_profesor = pk_profesor)
        if request.method == 'GET':
            formProfesor = FormProfesor(instance = clsProfesor)
        else:
            formProfesor = FormProfesor(request.POST, instance = clsProfesor)
            if formProfesor.is_valid():
                formProfesor.save()
                return redirect('HomeProfesor')
    except ObjectDoesNotExist as e:
        Error = e
    return render(request, 'TempProfesor/InsertProfesor.html', {'formProfesor':formProfesor, 'Error':Error, 'clsProfesor':clsProfesor})

def FindUpdateProfesor(request):
    if request.method == 'GET':
        return render(request, 'TempProfesor/FindProfesor.html')
    if request.method == 'POST':
        return redirect('UpdateProfesor', request.POST.get('pk_profesor'))

def DeleteProfesor(request, pk_profesor):
    Error = None
    clsProfesor = None
    try:
        clsProfesor = ClsProfesor.objects.get(pk_profesor = pk_profesor)
        if request.method == 'POST':
#   Este metodo elimina directamente a la DB
#   clsEstablecimiento.delete()
            clsProfesor.estado = 0
            clsProfesor.save()
            return redirect('HomeProfesor')
    except Exception as e:
        Error = "No se encontro ningun registro con ", pk_profesor
    return render(request, 'TempProfesor/DeleteProfesor.html', {'clsProfesor':clsProfesor, 'Error':Error})

def FindDeleteProfesor(request):
    if request.method == 'GET':
        return render(request, 'TempProfesor/FindProfesor.html')
    if request.method == 'POST':
        return redirect('DeleteProfesor', request.POST.get('pk_profesor'))

