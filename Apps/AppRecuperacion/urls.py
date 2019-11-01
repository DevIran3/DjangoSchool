from django.urls import path
from Apps.AppUsuario.views import Administrativo
from .views import HomeRecuperacion, SelectRecuperacion, InsertRecuperacion, FindUpdateRecuperacion, UpdateRecuperacion, FindDeleteRecuperacion, DeleteRecuperacion

urlpatterns = [

    path('Administrativo', Administrativo, name = 'Administrativo'),

    path('Inicio/', HomeRecuperacion, name ='HomeRecuperacion'),
    path('SeleccionarRecuperacion/', SelectRecuperacion, name = 'SelectRecuperacion'),
    path('InsertarRecuperacion/', InsertRecuperacion, name = 'InsertRecuperacion'),
    path('ActualizarRecuperacion/<int:pk_recuperacion>', UpdateRecuperacion, name = 'UpdateRecuperacion'),
    path('BuscarActualizarRecuperacion/', FindUpdateRecuperacion, name = 'FindUpdateRecuperacion'),
    path('EliminarRecuperacion/<int:pk_recuperacion>', DeleteRecuperacion, name = 'DeleteRecuperacion'),
    path('BuscarEliminarRecuperacion/', FindDeleteRecuperacion, name = 'FindDeleteRecuperacion'),
]