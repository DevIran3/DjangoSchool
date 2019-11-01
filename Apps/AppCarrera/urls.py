from django.urls import path
from Apps.AppUsuario.views import Administrativo
from .views import HomeCarrera, SelectCarrera, InsertCarrera, FindUpdateCarrera, UpdateCarrera, DeleteCarrera, FindDeleteCarrera

urlpatterns = [

    path('Administrativo', Administrativo, name = 'Administrativo'),

    path('Inicio/', HomeCarrera, name ='HomeCarrera'),
    path('SeleccionarCarrera/', SelectCarrera, name = 'SelectCarrera'),
    path('InsertarCarrera/', InsertCarrera, name = 'InsertCarrera'),
    path('BuscarActualizarCarrera/', FindUpdateCarrera, name = 'FindUpdateCarrera'),
    path('ActualizarCarrera/<int:id>', UpdateCarrera, name = 'UpdateCarrera'),
    path('BuscarEliminarCarrera/', FindDeleteCarrera, name = 'FindDeleteCarrera'),
    path('ElimiarCarrera/<int:id>', DeleteCarrera, name = 'DeleteCarrera'),
]