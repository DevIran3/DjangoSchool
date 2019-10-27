from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import ClsAlumno
from .forms import FormAlumno
from Apps.AppCarrera.models import ClsCarrera
from Apps.AppUsuario.models import ClsUsuario

# Create your views here.

def Home(request):
    return render(request, 'TempAlumno/index.html')

def SelectAlumno(request):
    clsAlumno = ClsAlumno.objects.filter(estado = 1)
    return render(request, 'TempAlumno/SelectAlumno.html', {'clsAlumno': clsAlumno})

def InsertAlumno(request):
    if request.method == 'POST':
        _nombre = request.POST.get('nombre')
        _apellido = request.POST.get('apellido')
        _fecha_ingreso = request.POST.get('fecha_ingreso')
        _contacto = request.POST.get('contacto')
        _email = request.POST.get('email')
        _direccion = request.POST.get('direccion')
        _estado = request.POST.get('estado')
        _fk_carrera = request.POST.get('fk_carrera')
        _fk_usuario = request.POST.get('fk_usuario')
        clsAlumno = ClsAlumno(nombre = _nombre,
                              apellido = _apellido,
                              fecha_ingreso = _fecha_ingreso,
                              contacto = _contacto,
                              email = _email,
                              direccion = _direccion,
                              estado = _estado,
                              fk_carrera = ClsCarrera.objects.get(id = _fk_carrera),
                              fk_usuario = ClsUsuario.objects.get(pk_usuario = _fk_usuario))
        clsAlumno.save()
        return redirect('http://127.0.0.1:8000/Alumno/Inicio/')
    return render(request, 'TempAlumno/InsertAlumno.html')

def UpdateAlumno(request, pk_alumno):
    Error = None
    formAlumno = None
    try:
        clsAlumno = ClsAlumno.objects.get(pk_alumno = pk_alumno)
        if request.method == 'GET':
            formAlumno = FormAlumno(instance = clsAlumno)
        else:
            formAlumno = FormAlumno(request.POST, instance = clsAlumno)
            if formAlumno.is_valid():
                formAlumno.save()
                return redirect('http://127.0.0.1:8000/Alumno/Inicio/')
    except ObjectDoesNotExist as e:
        Error = e
    return render(request, 'TempAlumno/InsertAlumno.html', {'formAlumno':formAlumno, 'Error':Error, 'clsAlumno':clsAlumno})

def FindUpdateAlumno(request):
    if request.method == 'GET':
        return render(request, 'TempAlumno/FindAlumno.html')
    if request.method == 'POST':
        return redirect('UpdateAlumno', request.POST.get('pk_alumno'))

def DeleteAlumno(request, pk_alumno):
    Error = None
    clsAlumno = None
    try:
        clsAlumno = ClsAlumno.objects.get(pk_alumno = pk_alumno)
        if request.method == 'POST':
#   Este metodo elimina directamente a la DB
#   clsEstablecimiento.delete()
            clsAlumno.estado = 0
            clsAlumno.save()
            return redirect('http://127.0.0.1:8000/Alumno/Inicio/')
    except Exception as e:
        Error = "No se encontro ningun registro con ", pk_alumno
    return render(request, 'TempAlumno/DeleteAlumno.html', {'clsAlumno':clsAlumno, 'Error':Error})

def FindDeleteAlumno(request):
    if request.method == 'GET':
        return render(request, 'TempAlumno/FindAlumno.html')
    if request.method == 'POST':
        return redirect('DeleteAlumno', request.POST.get('pk_alumno'))