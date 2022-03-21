from django.urls import path
from . import views


urlpatterns = [
    path('', views.listado_posts, name='listado_posts'),
    path('listado-usuarios/', views.listado_usuarios, name='listado_usuarios'),
    path('crear-usuarios/', views.crear_usuario, name='crear_usuario'),
    path('buscar-usuarios/', views.editar_usuario, name='buscar_usuario'),
    path('borrar-usuarios/', views.borrar_usuario, name='borrar_usuario'),
    path('editar-usuarios/', views.buscar_usuario, name='editar_usuario'),
    path('listado-asesores/', views.listado_asesores, name='listado_asesores'),

]
