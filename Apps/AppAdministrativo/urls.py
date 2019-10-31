from django.urls import path
# .views import functions
from .views import FindDeleteAdministrativo, DeleteAdministrativo, HomeAdministrativo, SelectAdministrativo, InsertAdministrativo, FindUpdateAdministrativo, UpdateAdministrativo

urlpatterns = [
    path('Inicio/', HomeAdministrativo, name ='index'),
    path('SeleccionarAdministrativo/', SelectAdministrativo, name = 'SelectAdministrativo'),
    path('InsertarAdministrativo/', InsertAdministrativo, name = 'InsertAdministrativo'),
    path('ActualizarAdministrativo/<int:pk_administrativo>', UpdateAdministrativo, name = 'UpdateAdministrativo'),
    path('BuscarActualizarAdministrativo/', FindUpdateAdministrativo, name = 'FindUpdateAdministrativo'),
    path('EliminarAdministrativo/<int:pk_administrativo>', DeleteAdministrativo, name = 'DeleteAdministrativo'),
    path('BuscarEliminarAdministrativo/', FindDeleteAdministrativo, name = 'FindDeleteAdministrativo'),
]