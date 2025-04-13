from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import paciente
from .forms import pacienteForm

def listar_pacientes(request):

    obj_pacientes = paciente.objects.all()

    return render(request, 'listar_paciente.html', {'list_pacientes': obj_pacientes})

def cadastrar_paciente(request):

    if request.method == 'POST':

        print(f"Request POST: {request.POST}")  # Debugging line to check request data

        #form = pacienteForm(request.POST)

        form = pacienteForm(data={'nome': 'Erik Hitoshi', 'CPF': '313.671.308-75', 'dataNascimento': '06/07/1983', 'telefone': '(19) 9827-4170', 'email': 'eh.muranaka@gmail.com', 'cep': '13468-847', 'endereco': 'Rua Emílio Alfeo Cordenonssi', 'numero': '48'})
        print(form.is_valid())  # Deve ser True

        # if form.is_valid():

        #     print(f"Form Valido")  # Debugging line to check form data
        #     form.save()
        #     messages.success(request, "Paciente cadastrado com sucesso.")
        #     return redirect('listar_pacientes')
        # else:
        #     print(f"Form Invalido")
        #     print(f"Erro form: {form.errors}")
        #     messages.error(request, "Erro ao cadastrar paciente.")
    else:
        form = pacienteForm()

    return render(request, 'cadastrar_paciente.html', {'form': form})

def alterar_paciente(request, paciente_id):

    obj_paciente = get_object_or_404(paciente, id=paciente_id)

    if request.method == 'POST':
        form = pacienteForm(request.POST, instance=obj_paciente)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')
    else:
        form = pacienteForm(instance=obj_paciente)

    return render(request, 'alterar_paciente.html', {'form': form})

def excluir_paciente(request, paciente_id):

    obj_paciente = get_object_or_404(paciente, id=paciente_id)
    
    if request.method == 'POST':
        paciente.delete()
        messages.success(request, f"Paciente '{paciente.nome}' excluído com sucesso.")

        return redirect('listar_pacientes')
    
    return render(request, 'excluir_paciente.html', {'paciente': paciente})