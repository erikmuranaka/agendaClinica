from django.shortcuts import render, get_object_or_404, redirect
from .models import medico
from .forms import medicoForm

def listar_medicos(request):
    obj_medicos = medico.objects.all()
    return render(request, 'listar_medico.html', {'list_medicos': obj_medicos})

def cadastrar_medico(request):
    if request.method == 'POST':
        form = medicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_medicos')
    else:
        form = medicoForm()
    return render(request, 'cadastrar.html', {'form': form})