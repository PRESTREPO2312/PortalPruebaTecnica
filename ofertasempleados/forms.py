# ofertasempleados/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuario,Oferta

class RegistroForm(UserCreationForm):
    nombres = forms.CharField(max_length=30)
    apellidos = forms.CharField(max_length=30)
    descripcion_perfil = forms.CharField(max_length=255)
    identificacion = forms.CharField(max_length=15)
    telefono = forms.CharField(max_length=15)

    class Meta:
        model = User  # Usar el modelo User de auth
        fields = ('username', 'email', 'password1', 'password2',)

    def save(self, commit=True):
        # Guarda el usuario en la tabla auth_user
        user = super(RegistroForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.last_name=self.cleaned_data['nombres']
        user.last_name=self.cleaned_data['apellidos']
        if commit:
            user.save()

        # Guarda el resto de los datos en la tabla Usuario
        usuario = Usuario.objects.create(
            user=user,
            descripcion_perfil=self.cleaned_data['descripcion_perfil'],
            identificacion=self.cleaned_data['identificacion'],
            telefono=self.cleaned_data['telefono'],
        )

        return user

class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = ['titulo', 'descripcion','titulo','salario','habilidades' ,'empresa']

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)