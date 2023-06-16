from django.shortcuts import render
from .models import Taller,Cliente,Comentario,Moderador

# Funciones de redireccion


def irInicio(request):
    return render(request, 'inicio.html')

def irInicioSesion(request):
    return render(request, 'login.html')

def irCrearCuenta(request):
    return render(request, 'crearCuenta.html')

def irTablas(request):
    ta = Taller.objects.all()
    cl = Cliente.objects.all()
    co = Comentario.objects.all()
    mo = Moderador.objects.all()
    return render(request, 'tablas.html', {'ta': ta, 'cl': cl, 'mo': mo, 'co': co})