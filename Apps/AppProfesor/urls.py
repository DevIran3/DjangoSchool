from django.urls import path
# .views import functions
from .views import FindDeleteProfesor ,DeleteProfesor ,FindUpdateProfesor ,UpdateProfesor ,HomeProfesor, SelectProfesor, InsertProfesor

urlpatterns = [
    path('Inicio/', HomeProfesor, name ='index'),
    path('SeleccionarProfesor/', SelectProfesor, name = 'SelectProfesor'),
    path('InsertarProfesor/', InsertProfesor, name = 'InsertProfesor'),
    path('ActualizarProfesor/<int:pk_profesor>', UpdateProfesor, name = 'UpdateProfesor'),
    path('BuscarActualizarProfesor/', FindUpdateProfesor, name = 'FindUpdateProfesor'),
    path('EliminarProfesor/<int:pk_profesor>', DeleteProfesor, name = 'DeleteProfesor'),
    path('BuscarEliminarProfesor/', FindDeleteProfesor, name = 'FindDeleteProfesor'),
]