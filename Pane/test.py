import random
import string

def generar_codigo_alfanumerico():
    # Formatos de códigos posibles
    formatos = [
        '{}{}{}{}'.format(*random.sample(string.ascii_uppercase, 2), *random.sample(range(10), 4)),
        '{}{}{}{}{}'.format(*random.sample(string.ascii_uppercase, 4), *random.sample(range(10), 2))
    ]

    # Seleccionar un formato aleatorio
    codigo_aleatorio = random.choice(formatos)

    # Retornar el código alfanumérico generado
    return codigo_aleatorio

def imprimir_mensaje():
    for i in range(10):
        print(generar_codigo_alfanumerico())

imprimir_mensaje()