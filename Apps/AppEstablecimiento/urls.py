from django.urls import path
from .views import InsertEstablecimiento, Home

urlpatterns = [
    path('FormEstablecimiento/', InsertEstablecimiento, name = 'InsertEstablecimiento'),
    path('Home/', Home, name = 'index'),
]
