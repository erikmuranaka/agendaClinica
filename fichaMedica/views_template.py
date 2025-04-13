from django.shortcuts import render, get_object_or_404, redirect
from .models import fichaMedica
from .forms import fichaMedicaForm

def listar_fichas_medica(request):
    obj_ficha_medica = fichaMedica.objects.all()
    return render(request, 'listar_fichamedica.html', {'list_ficha_medica': obj_ficha_medica})

def cadastrar_ficha_medica(request):
    if request.method == 'POST':
        form = fichaMedicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_fichas_medica')
    else:
        form = fichaMedicaForm()
    return render(request, 'cadastrar.html', {'form': form})