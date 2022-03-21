from django.shortcuts import render
from .models import Asesor, Post, Usuario
# Create your views here.

def listado_posts(request):
    
    posts = Post.objects.all()
    
    datos = {
        'posts': posts
    }
    
    return render(request, 'usuarios/listado_posts.html', datos)

################# CRUD Usuarios


def listado_usuarios(request):
    
    usuarios = Usuario.objects.all()
    
    datos = {
        'usuarios': usuarios
    }
    
    return render(request, 'usuarios/listado_usuarios.html', datos)


def crear_usuario(request):
    return render(request, 'usuarios/crear_usuario.html', {})


def editar_usuario(request):
    return render(request, 'usuarios/editar_usuario.html', {})


def borrar_usuario(request):
    return render(request, 'usuarios/borrar_usuario.html', {})


def buscar_usuario(request):
    return render(request, 'usuarios/buscar_usuario.html', {})

################# CRUD Asesores

def listado_asesores(request):
    
    asesores = Asesor.objects.all()
    
    datos = {
        'asesores': asesores
    }
    
    return render(request, 'usuarios/listado_asesores.html', datos)