from django.shortcuts import render, get_object_or_404, redirect
from .models import contasPagar
from .forms import ContasPagarForm

def listar_contas_pagar(request):
    obj_contasPagar = contasPagar.objects.all()
    return render(request, 'listar_cp.html', {'list_contas_pagar': obj_contasPagar})

def cadastrar_contas_pagar(request):
    if request.method == 'POST':
        form = ContasPagarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_contas_pagar')
    else:
        form = ContasPagarForm()
    return render(request, 'cadastrar.html', {'form': form})