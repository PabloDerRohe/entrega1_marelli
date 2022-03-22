from django.shortcuts import redirect, render

from .forms import BuscarAsesor, BuscarPost, BuscarUsuario, UsuarioForm, PostForm, AsesorForm
from .models import Asesor, Post, Usuario

# Create your views here.

def listado_posts(request):
    
    posts = Post.objects.all()
    
    datos = {
        'posts': posts
    }
    
    return render(request, 'usuarios/listado_posts.html', datos)


def crear_post(request):
    
    if request.method == 'POST':
        formulario = PostForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_post = Post(
                titulo=data['titulo'],
                autor=data['autor'],
                contenido=data['contenido'],
                )
            nuevo_post.save()
            
            return redirect('listado_posts')
            
    formulario = PostForm()
    return render(
        request, 
        'usuarios/crear_post.html',
        {'formulario': formulario})


def buscar_post(request):
    
    post_buscados = []
    dato = request.GET.get('buscar_post', None)
            
    if dato is not None:
        post_buscados = Post.objects.filter(titulo=dato)
    
    buscador = BuscarPost()
        
    return render(
        request, "usuarios/buscar_post.html",
        {'buscador': buscador, 'post_buscados': post_buscados, 'dato': dato})
    

################# CRUD Usuarios


def listado_usuarios(request):
    
    usuarios = Usuario.objects.all()
    
    datos = {
        'usuarios': usuarios
    }
    
    return render(request, 'usuarios/listado_usuarios.html', datos)


def crear_usuario(request):
    
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_usuario = Usuario(
                nombre=data['nombre'],
                apellido=data['apellido'],
                email=data['email']
                )
            nuevo_usuario.save()
            
            return redirect('listado_usuarios')
            
    formulario = UsuarioForm()
    return render(
        request, 
        'usuarios/crear_usuario.html',
        {'formulario': formulario})
    
    
def buscar_usuario(request):
    
    usuarios_buscados = []
    dato = request.GET.get('buscar_usuario', None)
    
        
    if dato is not None:
        usuarios_buscados = Usuario.objects.filter(nombre=dato)
    
    buscador = BuscarUsuario()
        
    return render(
        request, "usuarios/buscar_usuario.html",
        {'buscador': buscador, 'usuarios_buscados': usuarios_buscados, 'dato': dato})



def editar_usuario(request, id):
    
    usuario = Usuario.objects.get(id=id)    
    
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data #Limpia informacion
            usuario.nombre = data['nombre']
            usuario.apellido = data['apellido']
            usuario.email = data['email']
            usuario.save()
            return redirect('listado_usuarios')
            
    formulario = UsuarioForm(
        initial={
            'nombre': usuario.nombre,
            'apellido': usuario.apellido,
            'email': usuario.email,
        }
    )
    return render(
        request, 'usuarios/editar_usuario.html',
        {'formulario': formulario, 'usuario': usuario})



def borrar_usuario(request, id):
    
    usuario = Usuario.objects.get(id=id)    
    usuario.delete()
    
    return redirect('listado_usuarios')
    

################# CRUD Asesores

def listado_asesores(request):
    
    asesores = Asesor.objects.all()
    
    datos = {
        'asesores': asesores
    }
    
    return render(request, 'usuarios/listado_asesores.html', datos)

def crear_asesor(request):
    
    if request.method == 'POST':
        formulario = AsesorForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_asesor = Asesor(
                nombre=data['nombre'],
                apellido=data['apellido'],
                email=data['email'],
                especialidad=data['especialidad']
                )
            nuevo_asesor.save()
            
            return redirect('listado_asesores')
            
    formulario = AsesorForm()
    return render(
        request, 
        'usuarios/crear_asesor.html',
        {'formulario': formulario})
    
    
def buscar_asesor(request):
    
    asesores_buscados = []
    dato = request.GET.get('buscar_asesor', None)
    
        
    if dato is not None:
        asesores_buscados = Asesor.objects.filter(nombre=dato)
    
    buscador = BuscarAsesor()
    
    return render(
        request, "usuarios/buscar_asesor.html",
        {'buscador': buscador, 'asesores_buscados': asesores_buscados, 'dato': dato})



def editar_asesor(request, id):
    
    asesor = Asesor.objects.get(id=id)
     
    
    if request.method == 'POST':
        formulario = AsesorForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data #Limpia informacion
            asesor.nombre = data['nombre']
            asesor.apellido = data['apellido']
            asesor.email = data['email']
            asesor.especialidad = data['especialidad']
            asesor.save()
            return redirect('listado_asesores')
            
    formulario = AsesorForm(
        initial={
            'nombre': asesor.nombre,
            'apellido': asesor.apellido,
            'email': asesor.email,
            'especialidad': asesor.especialidad,
        }
    )
    return render(
        request, 'usuarios/editar_asesor.html',
        {'formulario': formulario, 'asesor': asesor})



def borrar_asesor(request, id):
    
    asesor = Asesor.objects.get(id=id)    
    asesor.delete()
    
    return redirect('listado_asesores')
    
