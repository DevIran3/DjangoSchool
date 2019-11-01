from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import ClsCarrera
from .forms import FormCarrera

# Create your views here.

def HomeCarrera(request):
    return render(request, 'TempCarrera/index.html')

def SelectCarrera(request):
#    clsEstablecimientos = ClsEstablecimiento.objects.all()
    clsCarrera = ClsCarrera.objects.filter(estado = 1)
    return render(request, 'TempCarrera/SelectCarrera.html', {'clsCarrera': clsCarrera})

def InsertCarrera(request):
    if request.method == 'POST':
        print(request.POST)
        _descripcion = request.POST.get('descripcion')
        _grado = request.POST.get('grado')
        _seccion = request.POST.get('seccion')
        _estado = request.POST.get('estado')
        clsCarrera = ClsCarrera(descripcion = _descripcion, grado = _grado, seccion = _seccion, estado = _estado)
        print("UPDATE", _descripcion, _grado, _seccion, _estado)
        clsCarrera.save()
        return redirect('HomeCarrera')
    return render(request, 'TempCarrera/InsertCarrera.html')

def UpdateCarrera(request, id):
    Error = None
    CarreraForm = None
    try:
        clsCarrera = ClsCarrera.objects.get(id = id)
        print(clsCarrera.id, clsCarrera.descripcion, clsCarrera.grado, clsCarrera.seccion, clsCarrera.estado)
        if request.method == 'GET':
            CarreraForm = FormCarrera(instance = clsCarrera)
        else:
            CarreraForm = FormCarrera(request.POST, instance = clsCarrera)
            print("UPDATE",clsCarrera.id, clsCarrera.descripcion, clsCarrera.grado, clsCarrera.seccion, clsCarrera.estado)
            if CarreraForm.is_valid():
                CarreraForm.save()
                return redirect('HomeCarrera')
    except ObjectDoesNotExist as e:
        Error = e
    return render(request, 'TempCarrera/InsertCarrera.html', {'CarreraForm':CarreraForm, 'Error':Error})

def DeleteCarrera(request, id):
    Error = None
    clsCarrera = None
    try:
        clsCarrera = ClsCarrera.objects.get(id = id)
        if request.method == 'POST':
#Este metodo elimina directamente a la DB
#        clsEstablecimiento.delete()
            clsCarrera.estado = 0
            clsCarrera.save()
            return redirect('HomeCarrera')
    except Exception as e:
        Error = "No se encontro ningun registro con ", id
    return render(request, 'TempCarrera/DeleteCarrera.html', {'clsCarrera':clsCarrera, 'Error':Error})

def FindUpdateCarrera(request):
    if request.method == 'GET':
        return render(request, 'TempCarrera/FindCarrera.html')
    if request.method == 'POST':
        return redirect('UpdateCarrera', request.POST.get('id'))

def FindDeleteCarrera(request):
    if request.method == 'GET':
        return render(request, 'TempCarrera/FindCarrera.html')
    if request.method == 'POST':
        return redirect('DeleteCarrera', request.POST.get('id'))

