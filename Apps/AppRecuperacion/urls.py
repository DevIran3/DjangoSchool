from django.urls import path
from .views import Home, SelectRecuperacion, InsertRecuperacion, FindUpdateRecuperacion, UpdateRecuperacion, FindDeleteRecuperacion, DeleteRecuperacion

urlpatterns = [
    path('Inicio/', Home, name = 'index'),
    path('SeleccionarRecuperacion/', SelectRecuperacion, name = 'SelectRecuperacion'),
    path('InsertarRecuperacion/', InsertRecuperacion, name = 'InsertRecuperacion'),
    path('ActualizarRecuperacion/<int:pk_recuperacion>', UpdateRecuperacion, name = 'UpdateRecuperacion'),
    path('BuscarActualizarRecuperacion/', FindUpdateRecuperacion, name = 'FindUpdateRecuperacion'),
    path('EliminarRecuperacion/<int:pk_recuperacion>', DeleteRecuperacion, name = 'DeleteRecuperacion'),
    path('BuscarEliminarRecuperacion/', FindDeleteRecuperacion, name = 'FindDeleteRecuperacion'),
]