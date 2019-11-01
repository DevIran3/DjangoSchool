from django.urls import path
from Apps.AppUsuario.views import Administrativo, Login
from Apps.AppNota.views import SelectNotaProfesor
from .views import HomeCurso, SelectCurso, InsertCurso, UpdateCurso, FindUpdateCurso, DeleteCurso, FindDeleteCurso

urlpatterns = [

    path('Administrativo/', Administrativo, name = 'Administrativo'),
    path('Login/', Login, name = 'Login'),

    path('Inicio/', HomeCurso, name ='HomeCurso'),
    path('SeleccionarCurso/', SelectCurso, name = 'SelectCurso'),
    path('InsertarCurso/', InsertCurso, name = 'InsertCurso'),
    path('ActualizarCurso/<int:pk_curso>', UpdateCurso, name = 'UpdateCurso'),
    path('BuscarActualizarCurso/', FindUpdateCurso, name = 'FindUpdateCurso'),
    path('EliminarCurso/<int:pk_curso>', DeleteCurso, name = 'DeleteCurso'),
    path('BuscarEliminarCurso/', FindDeleteCurso, name = 'FindDeleteCurso'),

    path('SelectNotaProfesor/<int:pk_curso>', SelectNotaProfesor, name = 'SelectNotaProfesor'),
]