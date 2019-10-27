from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import ClsCurso
from Apps.AppProfesor.models import ClsProfesor
from Apps.AppCarrera.models import ClsCarrera
from .forms import FormCurso

# Create your views here.

def Home(request):
    return render(request, 'TempCurso/index.html')

def SelectCurso(request):
    clsCurso = ClsCurso.objects.all()
    return render(request, 'TempCurso/SelectCurso.html', {'clsCurso': clsCurso})

def InsertCurso(request):
    if request.method == 'POST':
        _descripcion = request.POST.get('descripcion')
        _hora_entrada = request.POST.get('hora_entrada')
        _hora_salida = request.POST.get('hora_salida')
        _fk_profesor = request.POST.get('fk_profesor')
        _fk_carrera = request.POST.get('fk_carrera')
        clsCurso = ClsCurso(descripcion = _descripcion,
                              hora_entrada = _hora_entrada,
                              hora_salida = _hora_salida,
                              fk_profesor = ClsProfesor.objects.get(pk_profesor = _fk_profesor),
                              fk_carrera = ClsCarrera.objects.get(id = _fk_carrera))
        clsCurso.save()
        return redirect('http://127.0.0.1:8000/Curso/Inicio/')
    return render(request, 'TempCurso/InsertCurso.html')

def UpdateCurso(request, pk_curso):
    Error = None
    formCurso = None
    try:
        clsCurso = ClsCurso.objects.get(pk_curso = pk_curso)
        if request.method == 'GET':
            formCurso = FormCurso(instance = clsCurso)
        else:
            formCurso = FormCurso(request.POST, instance = clsCurso)
            if formCurso.is_valid():
                formCurso.save()
                return redirect('http://127.0.0.1:8000/Curso/Inicio/')
    except ObjectDoesNotExist as e:
        Error = e
    return render(request, 'TempCurso/InsertCurso.html', {'formCurso':formCurso, 'Error':Error, 'clsCurso':clsCurso})

def FindUpdateCurso(request):
    if request.method == 'GET':
        return render(request, 'TempCurso/FindCurso.html')
    if request.method == 'POST':
        return redirect('UpdateCurso', request.POST.get('pk_curso'))

def DeleteCurso(request, pk_curso):
    Error = None
    clsCurso = None
    try:
        clsCurso = ClsCurso.objects.get(pk_curso = pk_curso)
        if request.method == 'POST':
#   Este metodo elimina directamente a la DB
#   clsEstablecimiento.delete()
            clsCurso.estado = 0
            clsCurso.save()
            return redirect('http://127.0.0.1:8000/Curso/Inicio/')
    except Exception as e:
        Error = "No se encontro ningun registro con el codigo", pk_curso
    return render(request, 'TempAdministrativo/DeleteAdministrativo.html', {'clsCurso':clsCurso, 'Error':Error})

def FindDeleteAdministrativo(request):
    if request.method == 'GET':
        return render(request, 'TempAdministrativo/FindAdministrativo.html')
    if request.method == 'POST':
        return redirect('DeleteAdministrativo', request.POST.get('pk_administrativo'))