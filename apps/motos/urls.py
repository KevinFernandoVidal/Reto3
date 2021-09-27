from django.urls import path
from .views import *
urlpatterns = [
    #Url de pagina de inicio
    path('', motos_view, name='motos'),

    #Sección para autenticación
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registro', registro_view, name='registro'),
    path('actualizar_persona/', actualizar_view, name='actualizar'),

    #Sección motos
    path('mis_motos/', mis_motos_view, name='mis_motos'),
    path('moto_agregar/', moto_agregar_view, name='moto_agregar'),
    path('moto_editar/<int:id_moto>/', moto_editar_view, name='moto_editar'),
    path('moto_eliminar/<int:id_moto>/', moto_eliminar_view, name='moto_eliminar'),
    path('moto_detalles/<int:id_moto>/', moto_detalles_view, name='moto_detalles'),

    #Sección mantenimiento
    path('mantenimientos/<int:id_moto>/', mantenimientos_view, name='mantenimientos'),
    path('mantenimiento_agregar/<int:id_moto>/', mantenimiento_agregar_view, name='mantenimiento_agregar'),
    path('mantenimiento_editar/<int:id_mantenimiento>/', mantenimiento_editar_view, name='mantenimiento_editar'),
    path('mantenimiento_eliminar/<int:id_mantenimiento>/', mantenimiento_eliminar_view, name='mantenimiento_eliminar'),
    path('mantenimiento_detalles/<int:id_mantenimiento>/', mantenimiento_detalles_view, name='mantenimiento_detalles'),

    #Sección Transferir moto
    path('traspasos/', traspasos_view, name='traspasos'),
    path('traspasar_moto/<int:id_moto>/<int:id_historial>/', traspasar_moto_view, name='traspasar_moto'),
    path('traspaso_aceptar/<int:id_historial>/', traspaso_aceptar_view, name='traspaso_aceptar'),
    path('traspaso_rechazar/<int:id_historial>/', traspaso_rechazar_view, name='traspaso_rechazar'),
]