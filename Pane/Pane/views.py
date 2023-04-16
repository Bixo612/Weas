from django.shortcuts import render

# Funciones de redireccion


def irInicio(request):
    return render(request, 'inicio.html')

def irInicioSesion(request):
    return render(request, 'login.html')

def irCrearCuenta(request):
    return render(request, 'crearCuenta.html')