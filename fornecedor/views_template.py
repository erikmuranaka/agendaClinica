from django.shortcuts import render, get_object_or_404, redirect
from .models import fornecedor
from .forms import fornecedorForm

def listar_fornecedores(request):
    obj_fornecedores = fornecedor.objects.all()
    return render(request, 'listar_fornecedor.html', {'list_fornecedores': obj_fornecedores})

def cadastrar_fornecedor(request):
    if request.method == 'POST':
        form = fornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_fornecedores')
    else:
        form = fornecedorForm()
    return render(request, 'cadastrar.html', {'form': form})