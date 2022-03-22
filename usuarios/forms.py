from django import forms
from django.contrib.auth.models import User


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
    
class BuscarPost(forms.Form):
    buscar_post = forms.CharField(label='Buscador', max_length=40)
    
class AsesorForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    especialidad = forms.CharField(max_length=30)
    
class BuscarAsesor(forms.Form):
    buscar_asesor = forms.CharField(label='Buscador', max_length=20)