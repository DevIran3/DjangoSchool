from django.urls import path
from .views import InsertEstablecimiento, Home, SelectEstablecimiento, UpdateEstablecimiento

urlpatterns = [
    path('Home/', Home, name = 'index'),
    path('InsertarEstablecimiento/', InsertEstablecimiento, name = 'InsertEstablecimiento'),
    path('SeleccionarEstablecimiento/' , SelectEstablecimiento, name = 'SelectEstablecimiento'),
    path('ActualizarEstablecimiento/<int:pk_establecimiento>', UpdateEstablecimiento, name = 'UpdateEstablecimiento'),
]

# pasar parametros por la url con PATH usa normal
#path('SeleccionarEstablecimiento/<int:pk>/<slug:name>' , SelectEstablecimiento, name = 'SelectEstablecimiento')
    
# pasar parametros por la url con RE_PATH usa expresiones regulares
#re_path(r'^SeleccionarEstablecimiento/(?P<id>\d+)' , SelectEstablecimiento, name = 'SelectEstablecimiento')
