from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from main.models import *
from django.core.exceptions import ValidationError, ObjectDoesNotExist


class LoginForm(forms.Form):#форма авторизации и аутентификации
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    login.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})


    def clean(self):
        login = self.cleaned_data['login']
        password = self.cleaned_data['password']

        if not User.objects.filter(username=login).exists():
            raise ValidationError('Пользователь не существует')
        user = User.objects.get(username=login)
        if user:
            if not user.check_password(password):
                raise ValidationError('Неверный пароль')

        return self.cleaned_data