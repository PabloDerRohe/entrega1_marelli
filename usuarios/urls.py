from django.urls import path
from . import views


urlpatterns = [
    path('', views.listado_usuarios, name='listado_usuarios'),
    path('crear-usuarios/', views.crear_usuario, name='listado_usuarios'),
    path('buscar-usuarios/', views.editar_usuario, name='listado_usuarios'),
    path('borrar-usuarios/', views.borrar_usuario, name='listado_usuarios'),
    path('editar-usuarios/', views.buscar_usuario, name='listado_usuarios'),
]
