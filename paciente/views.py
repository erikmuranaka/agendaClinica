from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import models
from .models import paciente as dadosdb
from .forms import pacienteForm as form

def listar(request):

    query = request.GET.get('search')  # Captura o valor do campo de pesquisa

    ativo_filter = 'on'
    
    obj_dados = dadosdb.objects.filter(ativo__icontains='True')

    return render(request, 'listar_paciente.html', {'list_dados': obj_dados, 'ativo': ativo_filter})

def pesquisar(request):

    query = request.GET.get('search')
    
    ativo_filter = request.GET.get('ativo')

    if query:
        obj_dados = dadosdb.objects.filter(
             models.Q(nome__icontains=query) | models.Q(cpf__icontains=query)
            )
    else:
        obj_dados = dadosdb.objects.filter()

    ## Valida filtro da tela, para trazer os ativos e inativos
    if ativo_filter == 'on':
        obj_dados = obj_dados.filter(ativo=True)
    elif ativo_filter == 'off':
        obj_dados = obj_dados.filter(ativo=False)
    
    return render(request, 'listar_paciente.html', {'list_dados': obj_dados, 'ativo': ativo_filter})

def cadastrar(request):

    if request.method == 'POST':

        formDados = form(request.POST)

        if formDados.is_valid():

            paciente_dados = formDados.save(commit=False)
            paciente_dados.ativo = True
            paciente_dados.save()

            messages.success(request, "Cadastrado realizado com sucesso.")
            return redirect('listar_paciente')
        else:
            print(f"Erro formDados: {formDados.errors}")
            messages.error(request, "Erro ao realizar o cadastro.")
    else:
        formDados = form()

    return render(request, 'cadastrar_paciente.html', {'form': formDados})

def alterar(request, id):

    obj_dados = get_object_or_404(dadosdb, id=id)

    if request.method == 'POST':
        formDados = form(request.POST, instance=obj_dados)
        
        if formDados.is_valid():
            formDados.save()
            return redirect('listar_paciente')
        else:
            print(f"Erro ao salvar a alteração: {formDados.errors}")
            messages.error(request, "Erro ao realizar a alteração")
    else:
        formDados = form(instance=obj_dados)

    return render(request, 'alterar_paciente.html', {'form': formDados})

def excluir(request, id):
    # Busca o paciente no banco de dados
    obj_dados = get_object_or_404(dadosdb, id=id)

    # Atualiza o campo 'ativo' para False
    obj_dados.ativo = False
    obj_dados.save()

    # Exibe uma mensagem de sucesso
    messages.success(request, f"'{obj_dados.nome}' foi excluido com sucesso.")

    return redirect('listar_paciente')
