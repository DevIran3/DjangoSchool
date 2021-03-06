from django.urls import path
from Apps.AppUsuario.views import Administrativo
from .views import FindDeleteEstablecimiento, FindUpdateEstablecimiento ,InsertEstablecimiento, HomeEstablecimiento, SelectEstablecimiento, UpdateEstablecimiento, DeleteEstablecimiento

urlpatterns = [

    path('SesionAdministrativo/', Administrativo, name = 'Administrativo'),

    path('HomeAdministrativo/', HomeEstablecimiento, name ='HomeEstablecimiento'),
    path('InsertarEstablecimiento/', InsertEstablecimiento, name = 'InsertEstablecimiento'),
    path('SeleccionarEstablecimiento/' , SelectEstablecimiento, name = 'SelectEstablecimiento'),
    path('ActualizarEstablecimiento/<int:pk_establecimiento>', UpdateEstablecimiento, name = 'UpdateEstablecimiento'),
    path('EliminarEstablecimiento/<int:pk_establecimiento>', DeleteEstablecimiento, name = 'DeleteEstablecimiento'),
    path('BuscarActualizarEstablecimiento/', FindUpdateEstablecimiento, name = 'FindUpdateEstablecimiento'),
    path('BuscarDeleteEstablecimiento/', FindDeleteEstablecimiento, name = 'FindDeleteEstablecimiento'),
]

# pasar parametros por la url con PATH usa normal
#path('SeleccionarEstablecimiento/<int:pk>/<slug:name>' , SelectEstablecimiento, name = 'SelectEstablecimiento')
    
# pasar parametros por la url con RE_PATH usa expresiones regulares
#re_path(r'^SeleccionarEstablecimiento/(?P<id>\d+)' , SelectEstablecimiento, name = 'SelectEstablecimiento')
