"""
EXCEPCIONES:
    Las excepciones son errores que ocurren durante la ejecución del programa.
    Estos errores surgen a pesar de que la sintáxis sea correcta.
    
    Ejemplo:
        - Acceder a una posición de una lista que sea superior a la logitud de esta.
        - Intentar abrir un fichero que no existe.
        - Convertir 'skdjfsk' a entero(int).
    
    Importante: Gestionar las excepciones nos permite que el c+odigo se siga ejecutando a pesar de que ocurran errores.
"""

# import logging

# def division(a, b):
    
#     try:
#         resultado = a / b
#         print(resultado)
#     except ZeroDivisionError:
#         print("No se puede dividir por cero")

# division(8, 2)
# division(8, 0)

#! Gestion de diferentes tipos de excepciones
# frutas = ["0-Platano", "1-Manzana", "2-Pomelo", "3-Melocoton"]

# def elegirFruta(listaFrutas):
#     try:
#         print(listaFrutas)
#         index = int(input("Elige una fruta: "))
#         print(f'Tu fruta favorita es: {listaFrutas[index]}')
#     except IndexError:
#         print(f"El indice es incorrecto. Debe estar entre 0 y {len(listaFrutas) - 1}")
#     except ValueError:
#         print("Tienes que poner un número entero")
        
# elegirFruta(frutas)
# elegirFruta(frutas)
# elegirFruta(frutas)


#! Excepcion Exception -> Las excepciones son objetos que heredan de la clase Exception
# frutas = ["0-Platano", "1-Manzana", "2-Pomelo", "3-Melocoton"]

# def elegirFruta(listaFrutas):
#     try:
#         print(listaFrutas)
#         index = int(input("Elige una fruta: "))
#         print(f'Tu fruta favorita es: {listaFrutas[index]}')
#     except Exception as errorRandom:
#         logging.exception("El error es el siguiente: ")

# elegirFruta(frutas)


#! Uso del Else, Finally, Raise
#! Vamos a sumar los números que nos pase un usuario separados por espacios
while True:
    try:
        total = 0
        sumandos = input("Escribe números separados por espacios: ")
        sumandos = sumandos.split()
        for num in sumandos:
            if num.isnumeric():
                total += float(num)
            else:
                raise ValueError("El valor no es un número")
    except ValueError:
        print("Los datos son incorrectos")
        print("Vuelve a introducir los números")
    else:
        print(f'El resultado de la suma es: {total}')   #! El else se ejecutara si el try termina sin ningun error
        break
    finally:
        print("Ha terminado la iteración")  #! El finally se ejecuta independientemente de si hay excepcion o no


