from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import models
from .models import contasReceber as dadosdb
from .forms import contasReceberForm as form
from medico.models import medico
from paciente.models import paciente
from planoSaude.models import planoSaude

def listar(request):

    obj_dados = dadosdb.objects.select_related('idMedico', 'idPaciente', 'idPlano').all()

    return render(request, 'listar_cr.html', {'list_dados': obj_dados})

def pesquisar(request):

    query = request.GET.get('search')
    
    if query:
        obj_dados = dadosdb.objects.filter(
             models.Q(nome__icontains=query) | models.Q(cpf__icontains=query)
            )
    else:
        obj_dados = dadosdb.objects.filter()

    return render(request, 'listar_cr.html', {'list_dados': obj_dados})

def cadastrar(request):

    if request.method == 'POST':

        formDados = form(request.POST)

        formaPagamento = request.POST.get('formaPagamento')

        print(f"Forma de pagamento: {formaPagamento}")

        if formDados.is_valid():

            cr_dados = formDados.save(commit=False)
            cr_dados.ativo = True
            cr_dados.save()

            messages.success(request, "Cadastrado realizado com sucesso.")
            return redirect('listar_cr')
        else:
            print(f"Erro formDados: {formDados.errors}")
            messages.error(request, "Erro ao realizar o cadastro.")
    else:
        formDados = form()

    obj_medico = medico.objects.filter(ativo=True)
    obj_paciente = paciente.objects.filter(ativo=True)
    obj_plano = planoSaude.objects.filter(ativo=True)

    return render(request, 'cadastrar_cr.html', {'form': formDados, 'medicos': obj_medico, 'pacientes': obj_paciente, 'planos': obj_plano})

def alterar(request, id):

    obj_dados = get_object_or_404(dadosdb, id=id)

    if request.method == 'POST':
        formDados = form(request.POST, instance=obj_dados)
        
        if formDados.is_valid():
            formDados.save()
            return redirect('listar_cr')
        else:
            print(f"Erro ao salvar a alteração: {formDados.errors}")
            messages.error(request, "Erro ao realizar a alteração")
    else:
        formDados = form(instance=obj_dados)

    return render(request, 'alterar_cr.html', {'form': formDados})

def excluir(request, id):
    # Busca o cr no banco de dados
    obj_dados = get_object_or_404(dadosdb, id=id)

    # Atualiza o campo 'ativo' para False
    obj_dados.ativo = False
    obj_dados.save()

    # Exibe uma mensagem de sucesso
    messages.success(request, f"'{obj_dados.nome}' foi excluido com sucesso.")

    return redirect('listar_cr')