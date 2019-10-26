from django.urls import path
from .views import Home, SelectCarrera, InsertCarrera, FindUpdateCarrera, UpdateCarrera, DeleteCarrera, FindDeleteCarrera

urlpatterns = [
    path('Inicio/', Home, name = 'index'),
    path('SeleccionarCarrera/', SelectCarrera, name = 'SelectCarrera'),
    path('InsertarCarrera/', InsertCarrera, name = 'InsertCarrera'),
    path('BuscarActualizarCarrera/', FindUpdateCarrera, name = 'FindUpdateCarrera'),
    path('ActualizarCarrera/<int:id>', UpdateCarrera, name = 'UpdateCarrera'),
    path('BuscarEliminarCarrera/', FindDeleteCarrera, name = 'FindDeleteCarrera'),
    path('ElimiarCarrera/<int:id>', DeleteCarrera, name = 'DeleteCarrera'),
]