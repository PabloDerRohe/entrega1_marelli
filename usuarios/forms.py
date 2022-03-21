from django import forms
from django.contrib.auth.models import User
from .models import Usuario


class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class BuscarUsuario(forms.Form):
    buscar_usuario = forms.CharField(label='Buscador', max_length=20)
    
class PostForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    autor = forms.ModelChoiceField(queryset=User.objects.all())
    contenido = forms.CharField(widget=forms.Textarea)
    
class AsesorForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    especialidad = forms.CharField(max_length=30)