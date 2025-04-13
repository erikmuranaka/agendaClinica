from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import planoSaude
from .forms import planoSaudeForm
from paciente.models import paciente

def listar_plano_saude(request):
    obj_planos = planoSaude.objects.all()

    return render(request, 'listar_plano.html', {'list_planos': obj_planos})

def cadastrar_plano_saude(request):
    if request.method == 'POST':
        form = planoSaudeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_plano_saude')
    else:
        form = planoSaudeForm()
    return render(request, 'cadastrar_plano.html', {'form': form})

def alterar_plano_saude(request, plano_id):
    plano = get_object_or_404(planoSaude, id=plano_id)
    if request.method == 'POST':
        form = planoSaudeForm(request.POST, instance=plano)
        if form.is_valid():
            form.save()
            return redirect('listar_plano_saude')
    else:
        form = planoSaudeForm(instance=plano)
    return render(request, 'alterar_plano.html', {'form': form})

def excluir_plano_saude(request, plano_id):
    plano = get_object_or_404(planoSaude, id=plano_id)
    
    # Validação: Verifica se o plano está vinculado a outras tabelas
    if paciente.objects.filter(idPlano=plano).exists():
        messages.error(request, f"Não é possível excluir o plano de saúde '{plano.nome}', pois ele está sendo usado no paciente.")
        return redirect('listar_plano_saude')
    
    if request.method == 'POST':
        plano.delete()
        messages.success(request, f"Plano de saúde '{plano.nome}' excluído com sucesso.")
        return redirect('listar_plano_saude')
    
    return render(request, 'excluir_plano.html', {'plano': plano})