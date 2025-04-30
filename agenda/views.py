from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import models
from .models import agenda as dadosdb
from .forms import agendaForm as form
from django.http import JsonResponse
from medico.models import medico
from paciente.models import paciente

def visualizar_calendario(request):

    obj_medico = None

    if 'medico_id' in request.session:
        medico_id = request.session['medico_id']
        try:
            obj_medico = medico.objects.get(id=medico_id)
        except medico.DoesNotExist:
            pass

    obj_paciente = paciente.objects.all()

    return render(request, 'calendario.html', {'medico_padrao': obj_medico, 'pacientes': obj_paciente})

def listar_consulta(request):

    consultas = dadosdb.objects.select_related('idMedico', 'idPaciente').all()

    if not consultas:
        eventos = []  # Lista vazia de eventos
    else:
        eventos = [
            {
                'title': f"{consulta.idPaciente.nome}",
                'start': f"{consulta.data}T{consulta.hora}",
                'telefone': f"{consulta.idPaciente.telefone}",
                'descricao': f"{consulta.descricao}",
            }
            for consulta in consultas
        ]

    return JsonResponse(eventos, safe=False)

def agendar_consulta(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        hora = request.POST.get('hora')
        descricao = request.POST.get('descricao')
        idMedico = request.POST.get('idMedico')
        idPaciente = request.POST.get('idPaciente')

        # Salva o novo evento no banco de dados
        dadosdb.objects.create(
            data=data,
            hora=hora,
            descricao=descricao,
            idMedico_id=idMedico,
            idPaciente_id=idPaciente
        )
        return redirect('visualizar_calendario')  # Redireciona para o calendário

def cadastrar_paciente(request):

    if request.method == 'POST':

        paciente_nome = request.POST.get('nomePaciente')
        cpf = request.POST.get('cpfPaciente')
        telefone = request.POST.get('telefonePaciente')

        try:
            print(f"Paciente já existe: {paciente.objects.filter(nome=paciente_nome).exists()}")

            paciente_obj, created = paciente.objects.get_or_create(
                nome=paciente_nome,
                cpf=cpf,
                telefone=telefone,
                ativo=True
            )
        except paciente.DoesNotExist:
            print("Paciente não existe, criando novo paciente")
            
            paciente_obj = paciente.objects.create(
                nome=paciente_nome,
                cpf=cpf,
                telefone=telefone,
                ativo=True
            )
            created = True

        agenda_data=request.POST.get('modal-data2')
        agenda_hora=request.POST.get('modal-hora2')
        agenda_descricao=request.POST.get('modal-descricao2')
        agenda_idMedico_id=request.POST.get('modal-medico2')

        dadosdb.objects.create(
            data=agenda_data,
            hora=agenda_hora,
            descricao=agenda_descricao,
            idMedico_id=agenda_idMedico_id,
            idPaciente=paciente_obj
        )

        messages.success(request, 'Consulta agendada com sucesso!')

        return redirect('visualizar_calendario')
