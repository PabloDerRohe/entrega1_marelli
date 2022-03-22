from django.urls import path
from . import views


urlpatterns = [
    path('', views.listado_posts, name='listado_posts'),
    path('crear-post/', views.crear_post, name='crear_post'),
    path('buscar-post/', views.buscar_post, name='buscar_post'),
    path('listado-usuarios/', views.listado_usuarios, name='listado_usuarios'),
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    path('buscar-usuario/', views.buscar_usuario, name='buscar_usuario'),
    path('borrar-usuario/<int:id>', views.borrar_usuario, name='borrar_usuario'),
    path('editar-usuario/<int:id>', views.editar_usuario, name='editar_usuario'),
    path('listado-asesores/', views.listado_asesores, name='listado_asesores'),
    path('buscar-asesor/', views.buscar_asesor, name='buscar_asesor'),
    path('crear-asesor/', views.crear_asesor, name='crear_asesor'),
    path('editar-asesor/<int:id>', views.editar_asesor, name='editar_asesor'),
    path('borrar-asesor/<int:id>', views.borrar_asesor, name='borrar_asesor'),

]
