from django.db.models import Q
from apps.motos.models import Moto
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import *
from .forms import *

def motos_view(request):
    lista = Historial.objects.filter()
    return render(request, 'motos/motos.html', locals())

def login_view(request):
    usu = ""
    cla = ""
    if request.method == 'POST':
        formulario = login_form(request.POST)
        if formulario.is_valid():
            usu = formulario.cleaned_data['usuario']
            cla = formulario.cleaned_data['clave']
            usuario =authenticate(username=usu, password=cla)
            if usuario is not None and usuario.is_active:
                login(request, usuario)
                return redirect('/')
            else:
                msj = 'Sus credenciales son incorrectas, verifique e intente nuevamente.'
    formulario = login_form()                 
    return render(request, 'motos/login.html', locals())

def logout_view(request):
    logout(request)
    return redirect ('/login/')

def registro_view(request):

    if request.method == 'POST':
        form_u = registro_form(request.POST)
        form_p = persona_form(request.POST, request.FILES)  
        if form_u.is_valid() and form_p.is_valid():
            correo =  form_u.cleaned_data['correo']
            clave_1 = form_u.cleaned_data['clave_1']
            clave_2 = form_u.cleaned_data['clave_2']
            u = User.objects.create_user(username= correo, password= clave_2, is_superuser=False, is_staff=True)        

            p= form_p.save(commit=False)
            u.save()
            p.id_usuario = u
            
            p.save()
            return redirect ('/login/')
    else: #GET
        form_u = registro_form()
        form_p = persona_form()
        return render(request, 'motos/registro.html', locals())        
    return render(request, 'motos/registro.html', locals())

def actualizar_view(request):
    persona = Persona.objects.get(id_usuario = request.user.id)
    if request.method == 'POST':
        formulario = persona_form(request.POST, request.FILES, instance=persona)
        if formulario.is_valid():
            formulario.save()
            return redirect('/')
    else:
        formulario = persona_form()
    return render(request, 'motos/actualizar_persona.html', locals())

def mis_motos_view(request):
    propietario = Persona.objects.get(id_usuario = request.user.id)
    lista = Historial.objects.filter(propietario = propietario, estado='En propiedad')
    return render(request, 'motos/mis_motos.html', locals())

def moto_agregar_view(request):
    usuario = Persona.objects.get(id_usuario = request.user)
    if request.method == 'POST':
        
        formulario = agregar_moto_form(request.POST, request.FILES)
        if formulario.is_valid():
            m = formulario.save(commit=False)
            propietario= Historial()
            propietario.moto = m 
            propietario.propietario = usuario
            m.save()
            propietario.save()
            
            return redirect('/mis_motos/')
    else:
        formulario = agregar_moto_form()
    return render(request, 'motos/moto_agregar.html', locals())

def moto_editar_view(request, id_moto):
    moto = Moto.objects.get(id = id_moto)
    if request.method == 'POST':
        formulario = agregar_moto_form(request.POST, request.FILES, instance=moto)
        if formulario.is_valid():
            formulario.save()
            return redirect('/mis_motos/')
    else:
        formulario=agregar_moto_form(instance=moto)
    return render(request, 'motos/moto_editar.html', locals())
           
def moto_eliminar_view(request, id_moto):
    moto = Moto.objects.get(id = id_moto)
    moto.delete()
    return redirect('/mis_motos/')   

def moto_detalles_view(request, id_moto):    
    object= Historial.objects.get(id= id_moto)
    f =  ''
    if object.estado == 'Vendida':
        f = 'Vendida' 
    return render(request, 'motos/moto_detalles.html', locals())

def mantenimientos_view(request, id_moto):
    lista = Mantenimientos.objects.filter(moto = id_moto)
    return render(request, 'motos/mantenimientos.html', locals())

def mantenimiento_agregar_view(request, id_moto):
    moto = Moto.objects.get(id = id_moto)
    usuario = Persona.objects.get(id_usuario = request.user)
    if request.method == 'POST':
        formulario = mantenimiento_agregar_form(request.POST, request.FILES)
        if formulario.is_valid():  
            h = formulario.save(commit=False)
            h.responsable = usuario 
            h.moto = moto 
            h.save()
            return redirect('/mantenimientos/{}'.format(moto.id))
    else:
        formulario = mantenimiento_agregar_form()
    return render(request, 'motos/mantenimiento_agregar.html', locals())

def mantenimiento_editar_view(request, id_mantenimiento):
    mantenimiento = Mantenimientos.objects.get(id = id_mantenimiento)
    if request.method == 'POST':
        formulario = mantenimiento_agregar_form(request.POST, instance=mantenimiento) 
        if formulario.is_valid():
            formulario.save()
            return redirect('/mantenimientos/{}'.format(mantenimiento.moto.id))
    else:
        formulario = mantenimiento_agregar_form(instance=mantenimiento)
    return render(request, 'motos/mantenimiento_editar.html', locals())

def mantenimiento_eliminar_view(request, id_mantenimiento):
    mantenimiento = Mantenimientos.objects.get(id = id_mantenimiento)
    moto = mantenimiento.moto.id
    mantenimiento.delete()
    return redirect('/mantenimientos/{}'.format(moto))  

def mantenimiento_detalles_view(request, id_mantenimiento):
    object = Mantenimientos.objects.get(id = id_mantenimiento)
    return render(request, 'motos/mantenimiento_detalles.html', locals())

def traspasos_view(request):
    lista = Historial.objects.filter(estado = 'Pendiente new', propietario__id_usuario = request.user)
    return render(request, 'motos/traspasos.html', locals())

def traspasar_moto_view(request, id_moto, id_historial):
    moto = Moto.objects.get(id = id_moto)
    historial = Historial.objects.get(moto = moto, id = id_historial)
    form_moto = traspasar_moto_form(request.POST)
    if request.method == 'POST':
        if form_moto.is_valid():
            m = form_moto.save(commit=False)
            m.moto = moto
            m.estado = 'Pendiente new'
            m.save()
            historial.estado = 'Pendiente old'
            historial.save()
            return redirect('/')
    else:
        form_moto = traspasar_moto_form()
    return render(request, 'motos/traspasar_moto.html',  locals())

def traspaso_aceptar_view(request, id_historial):
    historial = Historial.objects.get(id = id_historial, propietario__id_usuario = request.user)
    historial.estado = 'En propiedad'
    historial.save()
    propietario_anterior = Historial.objects.get(moto = historial.moto, estado = 'Pendiente old')
    propietario_anterior.estado = 'Vendida'
    propietario_anterior.save()
    return redirect( '/mis_motos/')
    
def traspaso_rechazar_view(request, id_historial):
    historial = Historial.objects.get(id = id_historial, propietario__id_usuario = request.user)
    historial.estado = 'Rechazada'
    historial.save()
    propietario_anterior = Historial.objects.get(moto = historial.moto, estado = 'Pendiente old')
    propietario_anterior.estado = 'En propiedad'
    propietario_anterior.save()
    return redirect( '/mis_motos/')