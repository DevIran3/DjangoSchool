from django.urls import path
from .views import InsertEstablecimiento, Home

urlpatterns = [
    path('Home/', Home, name = 'index'),
    path('InsertarEstablecimiento/', InsertEstablecimiento, name = 'InsertEstablecimiento'),
]
