from django.urls import path
from Apps.AppAdministrativo.views import HomeAdministrativo
from Apps.AppRecuperacion.views import HomeRecuperacion
from Apps.AppProfesor.views import HomeProfesor
from Apps.AppAlumno.views import HomeAlumno
from Apps.AppNota.views import HomeNota
from Apps.AppEstablecimiento.views import HomeEstablecimiento
from .views import Login, FindDeleteUsuario, DeleteUsuario ,FindUpdateUsuario ,HomeUsuario, SelectUsuario, InsertUsuario, UpdateUsuario

urlpatterns = [
    path('Inicio/', HomeUsuario, name ='HomeUsuario'),
    path('SesionEstablecimiento', HomeEstablecimiento, name = 'HomeEstablecimiento'),
    path('SesionNota', HomeNota, name = 'HomeNota'),
    path('SesionAlumno', HomeAlumno, name = 'HomeAlumno'),
    path('SesionProfesor', HomeProfesor, name = 'HomeProfesor'),
    path('SesionRecuperacion', HomeRecuperacion, name = 'HomeRecuperacion'),
    path('SesionAdministrativo/', HomeAdministrativo, name = 'HomeAdministrativo'),
    path('Sesion/', Login, name = 'Login'),
    path('SeleccionarUsuario/', SelectUsuario, name = 'SelectUsuario'),
    path('InsertarUsuario/', InsertUsuario, name = 'InsertUsuario'),
    path('ActualizarUsuario/<int:pk_usuario>', UpdateUsuario, name = 'UpdateUsuario'),
    path('BuscarActualizarUsuario/', FindUpdateUsuario, name = 'FindUpdateUsuario'),
    path('BuscarEliminarUsuario/', FindDeleteUsuario, name = 'FindDeleteUsuario'),
    path('EliminarUsuario/<int:pk_usuario>', DeleteUsuario, name = 'DeleteUsuario'),
]
