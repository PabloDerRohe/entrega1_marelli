from django.shortcuts import render

# Create your views here.


def listado_usuarios(request):
    return render(request, 'usuarios/listado_usuarios.html', {})


def crear_usuario(request):
    return render(request, 'usuarios/crear_usuario.html', {})


def editar_usuario(request):
    return render(request, 'usuarios/editar_usuario.html', {})


def borrar_usuario(request):
    return render(request, 'usuarios/borrar_usuario.html', {})


def buscar_usuario(request):
    return render(request, 'usuarios/buscar_usuario.html', {})