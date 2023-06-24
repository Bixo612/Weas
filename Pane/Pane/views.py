from django.shortcuts import render
from .models import Taller, Cliente, Comentario, Moderador

# Funciones de redireccion


def irInicio(request):
    return render(request, 'inicio.html')


def irInicioSesion(request):
    return render(request, 'login.html')


def irCrearCuenta(request):
    return render(request, 'crearCuenta.html')

################################################################


def irAgregarRegistros(request):
    return render(request, 'agregarRegistros.html')


def irTablas(request):
    ta = Taller.objects.all()
    cl = Cliente.objects.all()
    co = Comentario.objects.all()
    mo = Moderador.objects.all()
    return render(request, 'tablas.html', {'ta': ta, 'cl': cl, 'mo': mo, 'co': co})


def fx_agregar_taller(request):

    obj_rol             = request.POST["ta_rol"]
    obj_razon_social    = request.POST["ta_razon_social"]
    obj_direccion       = request.POST["ta_direccion"]
    obj_comuna          = request.POST["ta_comuna"]
    obj_telefono        = request.POST["ta_telefono"]
    obj_clave           = request.POST["ta_clave"]
    obj_email           = request.POST["ta_email"]

    try:
        Taller.objects.create(
            rol             = obj_rol,
            razon_social    = obj_razon_social,
            direccion       = obj_direccion,
            comuna          = obj_comuna,
            telefono        = obj_telefono,
            clave           = obj_clave,
            email           = obj_email)
    except:
        pass

    ta = Taller.objects.all()
    cl = Cliente.objects.all()
    co = Comentario.objects.all()
    mo = Moderador.objects.all()
    return render(request, 'tablas.html', {'ta': ta, 'cl': cl, 'mo': mo, 'co': co})

def fx_agregar_moderador(request):

    obj_nick    = request.POST["mo_nick"]
    obj_email   = request.POST["mo_email"]
    obj_clave   = request.POST["mo_clave"]

    try: 
        Moderador.objects.create(
            nick    = obj_nick,
            email   = obj_email,
            clave   = obj_clave)
    except:
        pass

    ta = Taller.objects.all()
    cl = Cliente.objects.all()
    co = Comentario.objects.all()
    mo = Moderador.objects.all()
    return render(request, 'tablas.html', {'ta': ta, 'cl': cl, 'mo': mo, 'co': co})
