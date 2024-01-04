from django import forms
from Salon.models import Users
from django.contrib.auth import get_user_model


class UserRegisterForm(forms.Form):
    surname = forms.CharField(label='Фамилия', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    name = forms.CharField(label='Имя', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    patronymic = forms.CharField(label='Отчество', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    date_birth = forms.DateField(label='Дата рождения', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    telephone = forms.CharField(label='Телефон', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    street = forms.CharField(label='Улица', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    house = forms.CharField(label='Дом', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Users
        fields = ['surname', 'name', 'patronymic', 'date_birth', 'telephone', 'email', 'street', 'house', 'password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой email уже существует")
        return email


class LoginUserForm(forms.Form):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))



