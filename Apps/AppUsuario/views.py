from functools import partial
from tkinter.tix import _dummyFileComboBox

from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import FormUsuario
from .models import ClsUsuario
from Apps.AppEstablecimiento.models import ClsEstablecimiento

# Create your views here.
from requests import request

def Home(request):
    return render(request, 'TempUsuario/index.html')

def SelectUsuario(request):
#    clsEstablecimientos = ClsEstablecimiento.objects.all()
    clsUsuario = ClsUsuario.objects.filter(estado = 1)

#   ESTO SOLO MUESTRA CUANDO USAMOS FILTER Y TENEMOS UNA FK_KEY  == EJEMP ; {NOMBRE, APELLIDO , EDAD, FK_SCHOOL}
#   EL FK_SCHOOL NO TRAE SOLO EL DATO DEL ID SINO UN OBJETO AL CUAL ESTA VINCULADO EN EL No.3 ASI ACCEDEMOS A LOS
#   VALORES DEL OBJETO QUE ESTA EN ESE MISMO FK_SCHOOL DE ESTA TUPLA

# 1   cls =ClsUsuario.objects.get(fk_school = 16)                           --> consulta y guardar en var
# 2   print("VALORES: " + str(ClsUsuario.objects.get(fk_school = 16)))      --> mostramos el objeto como tal
# 3   print("VALORES: " + str(cls.fk_school.nombre))                        --> accedemos a uno de los atributos
    return render(request, 'TempUsuario/SelectUsuario.html', {'clsUsuario': clsUsuario})

def InsertUsuario(request):
    if request.method == 'POST':
        print(request.POST)
        _codigo_usuario = request.POST.get('codigo_usuario')
        _contrasena= request.POST.get('contrasena')
        _estado = request.POST.get('estado')
        _fk_school = request.POST.get('fk_school')
        print (_codigo_usuario, _contrasena, _estado, _fk_school)
#       fk_school = ClsEstablecimiento.objects.get(pk_establecimiento = _fk_school)
#       --> LO ENVIAMOS ASI POR QUE LA FK NECESITA NO SOLO EL NUMERO SINO EL OBJETO COMO TAL YA QUE LLEVA SUS ATRIBUTOS
        clsUsuario = ClsUsuario(codigo_usuario = _codigo_usuario, contrasena = _contrasena, estado = _estado, fk_school = ClsEstablecimiento.objects.get(pk_establecimiento = _fk_school))
        clsUsuario.save()
        return redirect('http://127.0.0.1:8000/Usuario/Inicio/')
    return render(request, 'TempUsuario/InsertUsuario.html')

def UpdateUsuario(request, pk_usuario):
    Error = None
    UsuarioForm = None
    try:
        clsUsuario = ClsUsuario.objects.get(pk_usuario = pk_usuario)
        if request.method == 'GET':
            UsuarioForm = FormUsuario(instance = clsUsuario)
        else:
            UsuarioForm = FormUsuario(request.POST, instance = clsUsuario)
            if UsuarioForm.is_valid():
                UsuarioForm.save()
                return redirect('http://127.0.0.1:8000/Usuario/Inicio/')
    except ObjectDoesNotExist as e:
        Error = e
    return render(request, 'TempUsuario/InsertUsuario.html', {'UsuarioForm':UsuarioForm, 'Error':Error, 'clsUsuario':clsUsuario})

def FindUpdateUsuario(request):
    if request.method == 'GET':
        return render(request, 'TempUsuario/FindUpdateUsuario.html')
    if request.method == 'POST':
        return redirect('UpdateUsuario', request.POST.get('pk_usuario'))

def DeleteUsuario(request, pk_usuario):
    Error = None
    clsUsuario = None
    try:
        clsUsuario = ClsUsuario.objects.get(pk_usuario = pk_usuario)
        if request.method == 'POST':
#   Este metodo elimina directamente a la DB
#   clsEstablecimiento.delete()
            clsUsuario.estado = 0
            clsUsuario.save()
            return redirect('http://127.0.0.1:8000/Usuario/Inicio/')
    except Exception as e:
        Error = "No se encontro ningun registro con ", pk_usuario
    return render(request, 'TempUsuario/DeleteUsuario.html', {'clsUsuario':clsUsuario, 'Error':Error})

def FindDeleteUsuario(request):
    if request.method == 'GET':
        return render(request, 'TempUsuario/FindDeleteUsuario.html')
    if request.method == 'POST':
        return redirect('DeleteUsuario', request.POST.get('pk_usuario'))
