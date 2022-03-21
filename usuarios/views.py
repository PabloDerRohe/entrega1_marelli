from django.shortcuts import redirect, render

from usuarios.forms import BuscarUsuario, UsuarioForm, PostForm, AsesorForm
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
        # usuarios_buscados = Curso.objects.filter(nombre=dato)
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

################# DATOS REFERENCIA

""" 

def listado_estudiantes(request):
    
    listado_estudiantes = Estudiante.objects.all()
    
    return render(
        request, "clase/listado_estudiantes.html",
        {'listado_estudiantes': listado_estudiantes}
    )
    
def crear_estudiante(request):
    if request.method == 'POST':
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_estudiante = Estudiante(
                nombre=data['nombre'],
                apellido=data['apellido'],
                email=data['email']
                )
            nuevo_estudiante.save()
            # return render(
            # request, 'clase/listado_estudiantes.html',
            # {})
            return redirect('listado_estudiantes')
            
    formulario = EstudianteFormulario()
    return render(
        request, 'clase/crear_estudiante.html',
        {'formulario': formulario})
    
def actualizar_estudiante(request, id):
    
    estudiante = Estudiante.objects.get(id=id)    
    
    if request.method == 'POST':
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data #Limpia informacion
            estudiante.nombre = data['nombre']
            estudiante.apellido = data['apellido']
            estudiante.email = data['email']
            estudiante.save()
            return redirect('listado_estudiantes')
            
    formulario = EstudianteFormulario(
        initial={
            'nombre': estudiante.nombre,
            'apellido': estudiante.apellido,
            'email': estudiante.email,
        }
    )
    return render(
        request, 'clase/actualizar_estudiante.html',
        {'formulario': formulario, 'estudiante': estudiante})
    
def borrar_estudiante(request, id):
    
    estudiante = Estudiante.objects.get(id=id)    
    estudiante.delete()
    
    return redirect('listado_estudiantes') 

def formulario_curso(request):
    
    ## Sin formularios de django
    # print(request.method)
    # if request.method == 'POST':
    #     print(request.POST)
    #     nuevo_curso = Curso(nombre=request.POST['curso'], camada=request.POST['camada'])
    #     nuevo_curso.save()
    #     return render(request, 'indice/index.html', {'nuevo_curso': nuevo_curso})
        
    
    # return render(request, 'clase/formulario_curso.html', {})
    
    ## Con formularios de django
    if request.method == 'POST':
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_curso = Curso(nombre=data['curso'], camada=data['camada'])
            nuevo_curso.save()
            
    formulario = CursoFormulario()
    return render(request, 'clase/formulario_curso.html', {'formulario': formulario})

def busqueda_curso(request):
    cursos_buscados = []
    dato = request.GET.get('partial_curso', None)
    
    if dato is not None:
        # cursos_buscados = Curso.objects.filter(nombre=dato)
        cursos_buscados = Curso.objects.filter(nombre=dato)
    
    buscador = BusquedaCurso()
    return render(
        request, "clase/busqueda_curso.html",
        {'buscador': buscador, 'cursos_buscados': cursos_buscados, 'dato': dato}

"""