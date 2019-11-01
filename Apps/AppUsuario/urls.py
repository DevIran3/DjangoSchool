from django.urls import path
from Apps.AppEstablecimiento.views import HomeEstablecimiento
from Apps.AppCarrera.views import HomeCarrera
from Apps.AppAlumno.views import HomeAlumno
from Apps.AppProfesor.views import HomeProfesor
from Apps.AppCurso.views import HomeCurso
from Apps.AppNota.views import HomeNota
from Apps.AppRecuperacion.views import HomeRecuperacion
from .views import Administrativo, Login, FindDeleteUsuario, DeleteUsuario ,FindUpdateUsuario ,HomeUsuario, SelectUsuario, InsertUsuario, UpdateUsuario

urlpatterns = [
    path('Inicio/', HomeUsuario, name ='HomeUsuario'),
    path('SeleccionarUsuario/', SelectUsuario, name = 'SelectUsuario'),
    path('InsertarUsuario/', InsertUsuario, name = 'InsertUsuario'),
    path('ActualizarUsuario/<int:pk_usuario>', UpdateUsuario, name = 'UpdateUsuario'),
    path('BuscarActualizarUsuario/', FindUpdateUsuario, name = 'FindUpdateUsuario'),
    path('BuscarEliminarUsuario/', FindDeleteUsuario, name = 'FindDeleteUsuario'),
    path('EliminarUsuario/<int:pk_usuario>', DeleteUsuario, name = 'DeleteUsuario'),

    #PATH LOGIN
    path('Login/', Login, name = 'Login'),
    path('SesionAdministrativo/', Administrativo, name = 'Administrativo'),

    #PATH ADMINISTRATIVO
    path('HomeAdministrativo/', HomeEstablecimiento, name ='HomeEstablecimiento'),
    path('HomeCarrera/', HomeCarrera, name ='HomeCarrera'),
    path('HomeAlumno', HomeAlumno, name = 'HomeAlumno'),
    path('HomeProfesor', HomeProfesor, name = 'HomeProfesor'),
    path('HomeCurso', HomeCurso, name = 'HomeCurso'),
    path('HomeNota', HomeNota, name = 'HomeNota'),
    path('HomeRecuperacion', HomeRecuperacion, name = 'HomeRecuperacion'),
]
