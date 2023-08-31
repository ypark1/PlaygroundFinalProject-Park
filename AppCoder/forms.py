from django import forms
from .models import Libro, Comentario
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
 
#class FormularioNuevoLibro(forms.Form):
    #titulo = forms.CharField(max_length=200)
    #autor = forms.CharField(max_length=60)
    

class SearchForm(forms.Form):
    titulo = forms.CharField(required=False)
    
class FormularioNuevoLibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('usuario', 'titulo', 'libroCategoria', 'autor', 'editorial', 'edicion', 'descripcion', 'precio', 'telefonoContacto', 'emailContacto', 'imagenLibro')

        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'libroCategoria' : forms.Select(attrs={'class': 'form-control'}),
            'autor' : forms.TextInput(attrs={'class': 'form-control'}),
            'editorial' : forms.TextInput(attrs={'class': 'form-control'}),
            'edicion' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefonoContacto' : forms.TextInput(attrs={'class': 'form-control'}),
            'emailContacto' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class ActualizacionoLibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('titulo', 'libroCategoria', 'autor', 'editorial', 'edicion', 'descripcion', 'precio', 'telefonoContacto', 'emailContacto', 'imagenLibro')
        
        widgets = {
            'titulo' : forms.TextInput(attrs={'class': 'form-control'}),
            'libroCategoria' : forms.Select(attrs={'class': 'form-control'}),
            'autor' : forms.TextInput(attrs={'class': 'form-control'}),
            'editorial' : forms.TextInput(attrs={'class': 'form-control'}),
            'edicion' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control'}),
            'precio' : forms.TextInput(attrs={'class': 'form-control'}),
            'telefonoContacto' : forms.TextInput(attrs={'class': 'form-control'}),
            'emailContacto' : forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class UserCreationFormCustom(UserCreationForm):
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput())
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput())
    email = forms.EmailField()
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput())
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')

class FormularioEdicion(UserChangeForm):
    password = None
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')


class FormularioCambioPassword(PasswordChangeForm):
    old_password = forms.CharField(label=("Password Actual"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=("Nuevo Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=("Repita Nuevo Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
        }