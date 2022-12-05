from django.shortcuts import render, redirect
from formulario.forms import *


# Create your views here.
def cadastrar(request):

    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('formulario:cadastrar')

    else:
        form = FormularioForm()
    
    context = { 'form': form }

    return render(request, 'cadastrar.html', context)


def lista(request):

    lista_clientes = DadosPessoais.objects.all()

    context = {'lista_clientes': lista_clientes}

    return render(request, 'lista.html', context)

    
def editar(request,pk):
    cliente = DadosPessoais.objects.get(id=pk)
    form = FormularioForm(instance= cliente)
    context = {'form':form}

    if request.method=='POST':
        form = FormularioForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            return redirect('formulario:lista')
    return render(request, 'editar.html', context)


def deletar(request, pk):
    cliente = DadosPessoais.objects.get(id=pk)
    context = {'cliente':cliente}

    if request.method=='POST':
        cliente.delete()
        return redirect('formulario:lista')
    return render(request, 'deletar.html', context)