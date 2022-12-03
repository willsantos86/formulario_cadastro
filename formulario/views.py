from django.shortcuts import render, redirect
from formulario.forms import *


# Create your views here.
def cadastrar(request):

    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('formulario: cadastrar')

    else:
        form = FormularioForm()
    
    context = { 'form': form }

    return render(request, 'cadastrar.html', context)