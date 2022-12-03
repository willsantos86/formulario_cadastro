from django.forms import ModelForm
from .models import *

class FormularioForm(ModelForm):
    class Meta:
        model = DadosPessoais
        fields = ['nome', 'email', 'telefone', 'genero', 'data_nascimento',
                'cidade', 'estado', 'endereco']