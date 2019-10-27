from django.urls import path
from .views import Home, SelectCurso, InsertCurso, UpdateCurso, FindUpdateCurso

urlpatterns = [
    path('Inicio/', Home, name = 'index'),
    path('SeleccionarCurso/', SelectCurso, name = 'SelectCurso'),
    path('InsertarCurso/', InsertCurso, name = 'InsertCurso'),
    path('ActualizarCurso/<int:pk_curso>', UpdateCurso, name = 'UpdateCurso'),
    path('BuscarActualizarCurso/', FindUpdateCurso, name = 'FindUpdateCurso')
]