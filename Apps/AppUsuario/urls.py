from django.urls import path
from Apps.AppEstablecimiento.views import HomeEstablecimiento
from Apps.AppCarrera.views import HomeCarrera
from Apps.AppAlumno.views import HomeAlumno
from Apps.AppProfesor.views import HomeProfesor
from Apps.AppCurso.views import HomeCurso, CursoProfesor
from Apps.AppNota.views import HomeNota, SelectNotaAlumno
from Apps.AppRecuperacion.views import HomeRecuperacion
from .views import UpdateUsuarioProfesor, Profesor, Administrativo, Login, FindDeleteUsuario, DeleteUsuario ,FindUpdateUsuario ,HomeUsuario, SelectUsuario, InsertUsuario, UpdateUsuario

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
    path('SesionProfesor/', Profesor, name = 'Profesor'),

    #PATH ADMINISTRATIVO
    path('HomeAdministrativo/', HomeEstablecimiento, name ='HomeEstablecimiento'),
    path('HomeCarrera/', HomeCarrera, name ='HomeCarrera'),
    path('HomeAlumno', HomeAlumno, name = 'HomeAlumno'),
    path('HomeProfesor', HomeProfesor, name = 'HomeProfesor'),
    path('HomeCurso', HomeCurso, name = 'HomeCurso'),
    path('HomeNota', HomeNota, name = 'HomeNota'),
    path('HomeRecuperacion', HomeRecuperacion, name = 'HomeRecuperacion'),

    #PATH PROFESOR
    path('CursoProfesor/<int:pk_profesor>', CursoProfesor, name = 'CursoProfesor'),
    path('UpdateUsuarioProfesor/<int:fk_usuario>', UpdateUsuarioProfesor, name = 'UpdateUsuarioProfesor'),

    #PATH ALUMNO
    path('SelectNotaAlumno/<int:pk_alumno>', SelectNotaAlumno, name = 'SelectNotaAlumno')
]
