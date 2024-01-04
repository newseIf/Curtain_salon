from django.urls import path, include
from users import views
from django.contrib.auth import views


from .views import *

urlpatterns = [

    path('register/', register, name='register'),
    path('login/', views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', logout_user , name='logout'),
]