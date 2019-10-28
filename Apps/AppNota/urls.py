from django.urls import path
from .views import DeleteNota, FindDeleteNota, Home, SelectNota, InsertNota, UpdateNota, FindUpdateNota

urlpatterns = [
    path('Inicio/', Home, name = 'index'),
    path('SeleccionarNota/', SelectNota, name = 'SelectNota'),
    path('InsertarNota/', InsertNota, name = 'InsertNota'),
    path('ActualizarNota/<int:pk_nota>', UpdateNota, name = 'UpdateNota'),
    path('BuscarActualizarNota/', FindUpdateNota, name = 'FindUpdateNota'),
    path('EliminarNota/<int:pk_nota>', DeleteNota, name = 'DeleteNota'),
    path('BuscarEliminarNota/', FindDeleteNota, name = 'FindDeleteNota'),
]