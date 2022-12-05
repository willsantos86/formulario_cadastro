from django.urls import path
from .views import *

app_name = 'formulario'

urlpatterns = [
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('lista/', lista, name='lista'),
]