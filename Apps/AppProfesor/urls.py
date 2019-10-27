from django.urls import path
# .views import functions
from .views import FindDeleteProfesor ,DeleteProfesor ,FindUpdateProfesor ,UpdateProfesor ,Home, SelectProfesor, InsertProfesor

urlpatterns = [
    path('Inicio/', Home, name = 'index'),
    path('SeleccionarProfesor/', SelectProfesor, name = 'SelectProfesor'),
    path('InsertarProfesor/', InsertProfesor, name = 'InsertProfesor'),
    path('ActualizarProfesor/<int:pk_profesor>', UpdateProfesor, name = 'UpdateProfesor'),
    path('BuscarActualizarProfesor/', FindUpdateProfesor, name = 'FindUpdateProfesor'),
    path('EliminarProfesor/<int:pk_profesor>', DeleteProfesor, name = 'DeleteProfesor'),
    path('BuscarEliminarProfesor/', FindDeleteProfesor, name = 'FindDeleteProfesor'),
]