from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth.hashers import make_password

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Услуги', 'url_name': 'service'},
        {'title': 'Отзывы', 'url_name': 'comment'},
        ]


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            password = form.cleaned_data.get('password')
            use = Users(
                surname=form.cleaned_data['surname'],
                name=form.cleaned_data['name'],
                patronymic=form.cleaned_data['patronymic'],
                date_birth=form.cleaned_data['date_birth'],
                telephone=form.cleaned_data['telephone'],
                email=form.cleaned_data['email'],
                street=form.cleaned_data['street'],
                house=form.cleaned_data['house'],
                password=make_password(password),
            )
            use.save()
            surname = form.cleaned_data.get('surname')
            name = form.cleaned_data.get('name')
            messages.success(request, f'Пользователь {surname} {name} был успешно зарегистрирован!')
            return redirect('/')
    else:
        form = UserRegisterForm()

    return render(
        request,
        'users/registration.html',
        {'title': 'Страница регистрации',
         'form': form, 'menu': menu, 'title': 'Регистрация'
         }
    )


def logout_user(request):
    logout(request)
    return redirect('/')
