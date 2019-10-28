from django.urls import path
from .views import Home, SelectCurso, InsertCurso, UpdateCurso, FindUpdateCurso, DeleteCurso, FindDeleteCurso

urlpatterns = [
    path('Inicio/', Home, name = 'index'),
    path('SeleccionarCurso/', SelectCurso, name = 'SelectCurso'),
    path('InsertarCurso/', InsertCurso, name = 'InsertCurso'),
    path('ActualizarCurso/<int:pk_curso>', UpdateCurso, name = 'UpdateCurso'),
    path('BuscarActualizarCurso/', FindUpdateCurso, name = 'FindUpdateCurso'),
    path('EliminarCurso/<int:pk_curso>', DeleteCurso, name = 'DeleteCurso'),
    path('BuscarEliminarCurso/', FindDeleteCurso, name = 'FindDeleteCurso'),
]