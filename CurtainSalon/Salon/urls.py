from django.urls import path, include
from . import views
from .views import *



urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('comment/', comment, name='comment'),
    path('type/<int:type_id>/', show_type_product, name='type'),

]
