from apps.motos.models import *

def numero_traspasos(request):
    try:
        noti = Historial.objects.filter(estado = 'Pendiente new', propietario__id_usuario = request.user).count()
        if noti == 0:
            noti = ""
    except:
        noti = 0
    return noti

def my_processor(request):
        context = {'ctx_noti': numero_traspasos(request),}
        return context