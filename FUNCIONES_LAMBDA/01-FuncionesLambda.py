# FUNCIONES LAMBDA

#! Las funciones lambda son funciones anónimas:
    #? Permiten múltiples argumentos.
    #? Solo puede tener una expresión.
    #? Estructura: lambda arg1, arg2 : expression

#! Apartado 1: Definir una función lambda.
suma = lambda a, b : a + b
print(suma(5, 8))
print(suma(7, 3))

saludar = lambda nombre : print(f'Hola {nombre}')
saludar('Juan')
saludar('Ana')



#! Apaertado 2: Llamar funciones dentro de una lambda.
#? Podemos llamar otras funciones dentro de la expresion de la función lambda.
maximo = lambda a, b, c : f'El máximo entre {a}, {b}, {c} es {max(a, b, c)}'
print(maximo(3, 4, 5))
print(maximo(10, 99, -25))



#! Apartado 3: Funciones lambda dentro de funciones.
#? Podemos definir funciones lambda dentro de funciones convencionales.
#** Gracias a esto podemos definir funciones lambda con distintos parámetros.
def ponerPrefijo(prefijo):
    return lambda nombre : f"{prefijo} {nombre}"    #! En esta función lambda fijamos el prefijo

addMr = ponerPrefijo("Mr")
addSr = ponerPrefijo("Sr")
addMiss = ponerPrefijo("Miss")

print(addMr("Beethoven"))
print(addSr("Mozart"))
print(addMiss("Fryda"))

#! Otro ejemplo
def elevarA(exponente):
    return lambda base : base ** exponente

elevarCuadrado = elevarA(2)
elevarCubo = elevarA(3)

#! Aca pasamos los argumentos a la lambda
print(elevarCuadrado(4))
print(elevarCubo(3))

#! otro ejemplo
def multiplicar(numero):
    return lambda multiplo : multiplo * numero

multiplicacion = multiplicar(3)

print(multiplicacion(5))


