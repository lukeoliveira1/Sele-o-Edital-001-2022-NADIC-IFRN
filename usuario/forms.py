from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.contrib.auth.forms import UserCreationForm, UserModel


class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # não permitir emails repetidos
    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
