# FUNCIONES MAP Y FILTER
#! Son funciones que sirven para trabajar con objetos iterables.
#! Vienen incorporadas pro defecto con Python
#! Uso de la función filter para comprobar emails válidos en una lista
#! Uso de la función filter con una función lambda

#! Apartado 1: Función filter
#? filter (funcion, iterable). devuelvel un iterador
#? con los valores del iterable que cumplan la función

import math

#! Ejemplo: Comprobar si una dirección de email es válida
emails = [
    'juan@mail.com',
    'javier@mail.com',
    'mandarinas',
    'wikipedia.com'
]

# #** Una comprobación sería:
# emailsValidos = []
# for email in emails:
#     if '@' in email:
#         print(f'El email {email} es válido')
#         emailsValidos.append(email)
#     else:
#         print(f'El email {email} es inválido')

# print(emailsValidos)

#! Ahora haremos la validación usando la función filter
def evaluarEmail(email):
    
    #? if '@' in email:  #! Esta comprobación se puede definir de una mejor manera
    #?     return True
    #? else:
    #?     return False
    
    return '@' in email
    
#! emailsValidos = list(filter(evaluarEmail, emails))
#! print(emailsValidos)    #! Objeto iterador

emailsValidos = list(filter(lambda email: '@' in email, emails))
print(emailsValidos)

# print(next(emailsValidos))
# print(next(emailsValidos))
# print(next(emailsValidos))  #! Este nos enviaria una excepción


#! Apartado 2: Función map
#! map(funcion, iterable)
#! Ejecúta la función usando como parámetro
#! cada elemento del iterable

palabras = ('Dale', 'ub', 'buen', 'like', 'y', 'suscribete')
longitudes = list(map(lambda palabra: len(palabra), palabras))

print(longitudes)

#! Usando el módulo math
#! A partir de un eje x, calcular los valores de una función matemática
eje_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  #? Este será el valor de x
eje_xx = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]  #? Este será el valor de y
eje_y = list(map(lambda x, y: round(math.cos(x) + math.exp(y), 3), eje_x, eje_xx))
print(eje_y)




