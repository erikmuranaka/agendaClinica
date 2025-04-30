from medico.models import medico

def medico_padrao(request):
    obj_medico = None
    if 'medico_id' in request.session:
        medico_id = request.session['medico_id']
        try:
            obj_medico = medico.objects.get(id=medico_id)
        except medico.DoesNotExist:
            pass

    return {'medico_padrao': obj_medico}