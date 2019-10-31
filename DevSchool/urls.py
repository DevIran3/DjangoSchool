"""DevSchool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import HomeAdministrativo
    2. Add a URL to urlpatterns:  path('', HomeAdministrativo.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Recuperacion/', include('Apps.AppRecuperacion.urls')),
    path('Nota/', include('Apps.AppNota.urls')),
    path('Curso/', include('Apps.AppCurso.urls')),
    path('Profesor/', include('Apps.AppProfesor.urls')),
    path('Alumno/', include('Apps.AppAlumno.urls')),
    path('Carrera/', include('Apps.AppCarrera.urls')),
    path('Usuario/', include('Apps.AppUsuario.urls')),
    path('Establecimiento/', include('Apps.AppEstablecimiento.urls')),
    path('Administrativo/', include('Apps.AppAdministrativo.urls')),
]
