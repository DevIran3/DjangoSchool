from django.urls import path
from Apps.AppUsuario.views import Administrativo
# .views import functions
from .views import FindDeleteProfesor ,DeleteProfesor ,FindUpdateProfesor ,UpdateProfesor ,HomeProfesor, SelectProfesor, InsertProfesor

urlpatterns = [

    path('Administrativo', Administrativo, name = 'Administrativo'),

    path('Inicio/', HomeProfesor, name ='HomeProfesor'),
    path('SeleccionarProfesor/', SelectProfesor, name = 'SelectProfesor'),
    path('InsertarProfesor/', InsertProfesor, name = 'InsertProfesor'),
    path('ActualizarProfesor/<int:pk_profesor>', UpdateProfesor, name = 'UpdateProfesor'),
    path('BuscarActualizarProfesor/', FindUpdateProfesor, name = 'FindUpdateProfesor'),
    path('EliminarProfesor/<int:pk_profesor>', DeleteProfesor, name = 'DeleteProfesor'),
    path('BuscarEliminarProfesor/', FindDeleteProfesor, name = 'FindDeleteProfesor'),
]