from django.forms import forms


class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class BuscarUsuario(forms.Form):
    buscar_usuario = forms.CharField(label='Buscador', max_length=20)
    
class PostForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    contenido = forms.TextField()
    
class AsesorForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    especialidad = forms.CharField(max_length=30)