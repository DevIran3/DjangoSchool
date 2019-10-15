from django.urls import path, include
from Apps.AppEstablecimiento.views import Home

urlpatterns = [
    path('', Home, name = 'index')
]
