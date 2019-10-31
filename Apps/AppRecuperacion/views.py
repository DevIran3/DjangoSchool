from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import ClsRecuperacion
from .forms import FormRecuperacion
from Apps.AppCurso.models import ClsCurso
from Apps.AppCarrera.models import ClsCarrera
from Apps.AppProfesor.models import ClsProfesor
from Apps.AppEstablecimiento.models import ClsEstablecimiento
from Apps.AppAlumno.models import ClsAlumno
# Create your views here.

def HomeRecuperacion(request):
    return render(request, 'TempRecuperacion/index.html')

def SelectRecuperacion(request):
    clsRecuperacion = ClsRecuperacion.objects.filter(estado = 1)
    return render(request, 'TempRecuperacion/SelectRecuperacion.html', {'clsRecuperacion': clsRecuperacion})

def InsertRecuperacion(request):
    if request.method == 'POST':
        _final = request.POST.get('final')
        _fecha_ingreso = request.POST.get('fecha_ingreso')
        _fecha_modificacion = request.POST.get('fecha_modificacion')
        _fk_curso = request.POST.get('fk_curso')
        _fk_carrera = request.POST.get('fk_carrera')
        _fk_profesor = request.POST.get('fk_profesor')
        _fk_establecimiento = request.POST.get('fk_establecimiento')
        _fk_alumno = request.POST.get('fk_alumno')
        clsRecuperacion = ClsRecuperacion(final = _final,
                          fecha_ingreso = _fecha_ingreso,
                          fecha_modificacion = _fecha_modificacion,
                          fk_curso = ClsCurso.objects.get(pk_curso = _fk_curso),
                          fk_carrera = ClsCarrera.objects.get(id = _fk_carrera),
                          fk_profesor = ClsProfesor.objects.get(pk_profesor = _fk_profesor),
                          fk_establecimiento = ClsEstablecimiento.objects.get(pk_establecimiento = _fk_establecimiento),
                          fk_alumno = ClsAlumno.objects.get(pk_alumno = _fk_alumno)
                          )
        clsRecuperacion.save()
        return redirect('HomeRecuperacion')
    return render(request, 'TempRecuperacion/InsertRecuperacion.html')

def UpdateRecuperacion(request, pk_recuperacion):
    Error = None
    formRecuperacion = None
    try:
        clsRecuperacion = ClsRecuperacion.objects.get(pk_recuperacion = pk_recuperacion)
        if request.method == 'GET':
            formRecuperacion = FormRecuperacion(instance = clsRecuperacion)
        else:
            formRecuperacion = FormRecuperacion(request.POST, instance = clsRecuperacion)
            if formRecuperacion.is_valid():
                formRecuperacion.save()
                return redirect('http://127.0.0.1:8000/Recuperacion/Inicio/')
    except ObjectDoesNotExist as e:
        Error = e
    return render(request, 'TempRecuperacion/InsertRecuperacion.html', {'formRecuperacion':formRecuperacion, 'Error':Error, 'clsRecuperacion':clsRecuperacion})

def FindUpdateRecuperacion(request):
    if request.method == 'GET':
        return render(request, 'TempRecuperacion/FindRecuperacion.html')
    if request.method == 'POST':
        return redirect('UpdateRecuperacion', request.POST.get('pk_recuperacion'))

def DeleteRecuperacion(request, pk_recuperacion):
    Error = None
    clsRecuperacion = None
    try:
        clsRecuperacion = ClsRecuperacion.objects.get(pk_recuperacion = pk_recuperacion)
        if request.method == 'POST':
#   Este metodo elimina directamente a la DB
#   clsEstablecimiento.delete()
            clsRecuperacion.estado = 0
            clsRecuperacion.save()
            return redirect('http://127.0.0.1:8000/Recuperacion/Inicio/')
    except Exception as e:
        Error = "No se encontro ningun registro con el codigo", pk_recuperacion
    return render(request, 'TempRecuperacion/DeleteRecuperacion.html', {'clsRecuperacion':clsRecuperacion, 'Error':Error})

def FindDeleteRecuperacion(request):
    if request.method == 'GET':
        return render(request, 'TempRecuperacion/FindRecuperacion.html')
    if request.method == 'POST':
        return redirect('DeleteRecuperacion', request.POST.get('pk_recuperacion'))
