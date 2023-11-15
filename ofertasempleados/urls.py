from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import EmpresaViewSet, OfertaViewSet, UsuarioViewSet, PostulacionViewSet,RegistroUsuario,CrearOfertaView,homes,user_login,logout_view
from django.urls import path,include


router = routers.DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'ofertas', OfertaViewSet, basename='oferta')
router.register(r'postulaciones', PostulacionViewSet)

urlpatterns = [
    path('', homes, name='homes'),
    path('', include(router.urls)),
    path('registro/', RegistroUsuario.as_view(), name='registro'),
    path('crear-oferta/', CrearOfertaView.as_view(), name='crear_oferta'),
    path('login/', user_login, name='login'),
    path('logout/', logout_view, name='logout')

]



