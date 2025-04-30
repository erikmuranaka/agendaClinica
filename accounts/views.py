from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from medico.models import medico

def login_medico(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('senha')
        medico_id = request.POST.get('medico')

        # Autenticação do usuário
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Loga o usuário no sistema
            
            # Armazena o médico selecionado na sessão
            request.session['medico_id'] = medico_id
            return redirect('listar_paciente')  # Redireciona para a página inicial ou dashboard
        else:
            print('Usuário ou senha incorretos.')
            # Exibe mensagem de erro se login ou senha estiverem incorretos
            return render(request, 'login.html', {
                'medicos': medico.objects.all(),
                'error': 'Usuário ou senha incorretos.'
            })

    # Passa os médicos para o template
    medicos = medico.objects.all()
    return render(request, 'login.html', {'medicos': medicos})