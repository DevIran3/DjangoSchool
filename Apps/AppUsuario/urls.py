from django.urls import path
from .views import FindDeleteUsuario ,DeleteUsuario ,FindUpdateUsuario ,Home, SelectUsuario, InsertUsuario, UpdateUsuario

urlpatterns = [
    path('Inicio/', Home, name = 'index'),
    path('SeleccionarUsuario/', SelectUsuario, name = 'SelectUsuario'),
    path('InsertarUsuario/', InsertUsuario, name = 'InsertUsuario'),
    path('ActualizarUsuario/<int:pk_usuario>', UpdateUsuario, name = 'UpdateUsuario'),
    path('BuscarActualizarUsuario/', FindUpdateUsuario, name = 'FindUpdateUsuario'),
    path('BuscarEliminarUsuario/', FindDeleteUsuario, name = 'FindDeleteUsuario'),
    path('EliminarUsuario/<int:pk_usuario>', DeleteUsuario, name = 'DeleteUsuario'),
]
