from django.urls import path
from .views import InsertEstablecimiento, Home, SelectEstablecimiento

urlpatterns = [
    path('Home/', Home, name = 'index'),
    path('InsertarEstablecimiento/', InsertEstablecimiento, name = 'InsertEstablecimiento'),
    path('SeleccionarEstablecimiento/' , SelectEstablecimiento, name = 'SelectEstablecimiento')
]
