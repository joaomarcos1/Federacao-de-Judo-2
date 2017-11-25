from django import forms
from django.contrib.auth.models import User
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm 

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    telefone = forms.IntegerField(required=True)
    endereco = forms.CharField(max_length=50,label='N')

    #tipo_usuario = forms.CharField(max_length=30)
    #data_nascimento = forms.DateTimeField(required=True)
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            )
    def save(self, commit=True):
    	usuario = Usuario()
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.telefone =self.cleaned_data['telefone']
        user.endereco=self.cleaned_data['endereco']
        usuario.setTelefone(self.cleaned_data['telefone'])
        usuario.setEndereco(self.cleaned_data['endereco'])
        if commit:
            user.save()
            usuario.save()

        return user