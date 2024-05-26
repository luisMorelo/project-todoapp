from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, AuthenticationForm, UsernameField
)
from django.contrib.auth.models import User


#Registrarse/crear una cuenta
class SingUpForm(UserCreationForm):
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='confirmar contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User #el modelo que voy a usar
        fields = ['username','first_name', 'last_name', 'email'] #los campos del modelo que voy a usar

        #aqui se definen las etiquetas para cada uno de los campos 
        labels= {
            "first_name": "nombre",
            "last_name": "apellido",
            "email": "correo"
        }

        #Aqui se establece el tipo de etiquetas que van a tener los campos en el formulario, eso se conoce como widgets
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class":"form-control"})
        }

#Acceso/inicio de secion 
class LoginFoms(AuthenticationForm):
    username = UsernameField(widget=forms.TimeInput(attrs={"autofocus": True, "class": "form-control"}))
    password = forms.CharField(
        label= "contraseña",
        strip= True, #esto es para quitar los espacios en la contraseñas dijitada por el usuario
        widget=forms.PasswordInput(attrs={"autocompleted":"current-password", "class": "form-control"}) 
    )