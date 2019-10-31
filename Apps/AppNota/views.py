from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import ClsNota
from .forms import FormNota
from Apps.AppCurso.models import ClsCurso
from Apps.AppCarrera.models import ClsCarrera
from Apps.AppProfesor.models import ClsProfesor
from Apps.AppEstablecimiento.models import ClsEstablecimiento
from Apps.AppAlumno.models import ClsAlumno


# Create your views here.

def HomeNota(request):
    return render(request, 'TempNota/index.html')

def SelectNota(request):
    clsNota = ClsNota.objects.filter(estado = 1)
    return render(request, 'TempNota/SelectNota.html', {'clsNota': clsNota})

def InsertNota(request):
    if request.method == 'POST':
        _parcial_1 = request.POST.get('parcial_1')
        _parcial_2 = request.POST.get('parcial_2')
        _zona = request.POST.get('zona')
        _parcial_3 = request.POST.get('parcial_3')
        _final = request.POST.get('final')
        _fecha_ingreso = request.POST.get('fecha_ingreso')
        _fecha_modificacion = request.POST.get('fecha_modificacion')
        _fk_curso = request.POST.get('fk_curso')
        _fk_carrera = request.POST.get('fk_carrera')
        _fk_profesor = request.POST.get('fk_profesor')
        _fk_establecimiento = request.POST.get('fk_establecimiento')
        _fk_alumno = request.POST.get('fk_alumno')
        clsNota = ClsNota(parcial_1 = _parcial_1,
                          parcial_2 = _parcial_2,
                          zona = _zona,
                          parcial_3 = _parcial_3,
                          final = _final,
                          fecha_ingreso = _fecha_ingreso,
                          fecha_modificacion = _fecha_modificacion,
                          fk_curso = ClsCurso.objects.get(pk_curso = _fk_curso),
                          fk_carrera = ClsCarrera.objects.get(id = _fk_carrera),
                          fk_profesor = ClsProfesor.objects.get(pk_profesor = _fk_profesor),
                          fk_establecimiento = ClsEstablecimiento.objects.get(pk_establecimiento = _fk_establecimiento),
                          fk_alumno = ClsAlumno.objects.get(pk_alumno = _fk_alumno)
                          )
        clsNota.save()
        return redirect('HomeNota')
    return render(request, 'TempNota/InsertNota.html')

def UpdateNota(request, pk_nota):
    Error = None
    formNota = None
    try:
        clsNota = ClsNota.objects.get(pk_nota = pk_nota)
        if request.method == 'GET':
            formNota = FormNota(instance = clsNota)
        else:
            formNota = FormNota(request.POST, instance = clsNota)
            if formNota.is_valid():
                formNota.save()
                return redirect('HomeNota')
    except ObjectDoesNotExist as e:
        Error = e
    return render(request, 'TempNota/InsertNota.html', {'formNota':formNota, 'Error':Error, 'clsNota':clsNota})

def FindUpdateNota(request):
    if request.method == 'GET':
        return render(request, 'TempNota/FindNota.html')
    if request.method == 'POST':
        return redirect('UpdateNota', request.POST.get('pk_nota'))

def DeleteNota(request, pk_nota):
    Error = None
    clsNota = None
    try:
        clsNota = ClsNota.objects.get(pk_nota = pk_nota)
        if request.method == 'POST':
#   Este metodo elimina directamente a la DB
#   clsEstablecimiento.delete()
            clsNota.estado = 0
            clsNota.save()
            return redirect('HomeNota')
    except Exception as e:
        Error = "No se encontro ningun registro con el codigo", pk_nota
    return render(request, 'TempNota/DeleteNota.html', {'clsNota':clsNota, 'Error':Error})

def FindDeleteNota(request):
    if request.method == 'GET':
        return render(request, 'TempNota/FindNota.html')
    if request.method == 'POST':
        return redirect('DeleteNota', request.POST.get('pk_nota'))
