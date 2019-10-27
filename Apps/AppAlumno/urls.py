from django.urls import path
# .view import funciones
from .views import Home, InsertAlumno, SelectAlumno, FindUpdateAlumno, UpdateAlumno, FindDeleteAlumno, DeleteAlumno

urlpatterns = [
    path('Inicio/', Home, name = 'index'),
    path('SeleccionarAlumno/', SelectAlumno, name = 'SelectAlumno'),
    path('InsertarAlumno/', InsertAlumno, name = 'InsertAlumno'),
    path('ActualizarAlumno/<int:pk_alumno>', UpdateAlumno, name = 'UpdateAlumno'),
    path('BuscarActulizarAlumno/', FindUpdateAlumno, name = 'FindUpdateAlumno'),
    path('BuscarEliminarAlumno/<int:pk_alumno>', DeleteAlumno, name = 'DeleteAlumno'),
    path('BuscarEliminarAlumno/', FindDeleteAlumno, name = 'FindDeleteAlumno'),
]