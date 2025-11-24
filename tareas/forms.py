from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormularioTarea(forms.Form):
    """Formulario para crear/editar tareas"""
    titulo = forms.CharField(
        max_length=200,
        label="Título",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa el título de la tarea'
        })
    )
    descripcion = forms.CharField(
        label="Descripción",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Ingresa la descripción detallada'
        })
    )


class RegistroForm(UserCreationForm):
    """Formulario de registro personalizado"""
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'correo@ejemplo.com'
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre usuario'
        })
    )
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña'
        })
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')