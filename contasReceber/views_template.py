from django.shortcuts import render, get_object_or_404, redirect
from .models import contasReceber
from .forms import contasReceberForm

def listar_contas_receber(request):
    obj_contas_receber = contasReceber.objects.all()
    return render(request, 'listar_cr.html', {'list_contas_receber': obj_contas_receber})

def cadastrar_contas_receber(request):
    if request.method == 'POST':
        form = contasReceberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_contas_receber')
    else:
        form = contasReceberForm()
    return render(request, 'cadastrar.html', {'form': form})