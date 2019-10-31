from django.urls import path
# .view import funciones
from .views import HomeAlumno, InsertAlumno, SelectAlumno, FindUpdateAlumno, UpdateAlumno, FindDeleteAlumno, DeleteAlumno

urlpatterns = [
    path('Inicio/', HomeAlumno, name ='HomeAlumno'),
    path('SeleccionarAlumno/', SelectAlumno, name = 'SelectAlumno'),
    path('InsertarAlumno/', InsertAlumno, name = 'InsertAlumno'),
    path('ActualizarAlumno/<int:pk_alumno>', UpdateAlumno, name = 'UpdateAlumno'),
    path('BuscarActulizarAlumno/', FindUpdateAlumno, name = 'FindUpdateAlumno'),
    path('BuscarEliminarAlumno/<int:pk_alumno>', DeleteAlumno, name = 'DeleteAlumno'),
    path('BuscarEliminarAlumno/', FindDeleteAlumno, name = 'FindDeleteAlumno'),
]