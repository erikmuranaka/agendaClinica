from django.shortcuts import render, get_object_or_404, redirect
from .models import agenda
from .forms import agenda_form

def listar_agendas(request):
    obj_agendas = agenda.objects.all()
    return render(request, 'listar_agenda.html', {'list_agendas': obj_agendas})

def cadastrar_agenda(request):
    if request.method == 'POST':
        form = agenda_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_agendas')
    else:
        form = agenda_form()
    return render(request, 'cadastrar.html', {'form': form})