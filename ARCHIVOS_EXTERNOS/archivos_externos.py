# ARCHIVOS EXTERNOS

#! Por defecto, el modo de abrir un fichero es lectura
#! como texto. Por lo que para leer su contenido
#! no es necesario especificar el segundo argumento.

#! r -> read
#! w -> write
#! a -> append
#! x -> create

#! t -> text-mode
#! b -> bytes - para archivos como fotos

#! Abrimos el fichero
"""fichero = open('./ARCHIVOS_EXTERNOS/demo.txt', 'rt', encoding='utf-8')

primeraLinea = fichero.readline()
print(primeraLinea)
print(fichero.readline())
print(fichero.readline())
"""

"""fichero = open('./ARCHIVOS_EXTERNOS/demo.txt', 'rt', encoding='utf-8')

todasLasLineas = fichero.readlines()
print(todasLasLineas)"""

#! En este caso, leerá la primera línea como se indica en el primer print.
#! Después leerá las líneas restantes como se indica en el segundo print.
#fichero = open('./ARCHIVOS_EXTERNOS/demo.txt', 'rt', encoding='utf-8')
#print(fichero.readline())

#

#! El fichero se debe cerrar una vez lo hayamos abierto
#fichero.close()


#! Apartado 2: Escribir en un fichero existente
#! Si in fichero ya tiene contenido, tenemos dos opciones:
#! Sobreescribir el contenido o, añadir el contenido nuevo
#! al final del que ya existe -> Modo Write.

# fichero = open('./ARCHIVOS_EXTERNOS/demo.txt', 'w', encoding='utf-8')
# fichero.write('Me he cargado todo lo que había.\n')
# listaContenido = [
#     'Esta es una prueba de adicion de informacion.',
#     'Se entenderá el correcto funcionamiento de método write.',
#     'Animo Pythoneros.'
# ]
#! Con esta instrucción añadimos los saltos de línea
# listaContenido = map(lambda line: line + '\n', listaContenido)

# fichero.writelines(listaContenido)
# fichero.close()

#! Apartado 3: Escribir en un fichero existente
#! Modo append. Nos sirve para añadir contenido
#! sin eliminar el existente.

# fichero = open('./ARCHIVOS_EXTERNOS/demo.txt', 'a', encoding='utf-8')
# fichero.write('\n\n\nEsto es una nueva linea')
# fichero.close()


#! Apartado 4: Crear un nuevo fichero.
#! Cuando usamos open en modo create, podemos
#! podemos escribir en el ficehro tras crearlo
#! pero no leer

# fichero = open('./ARCHIVOS_EXTERNOS/demo2.txt', 'x', encoding='utf-8')
# fichero.write('Soy un fichero nuevo')

#! Con esta instrucción podemos ver si un archivo que vamos a crear se puede leer o editar
# print(fichero.readable())
# print(fichero.writable())

# fichero.close()


#! Apartado 5: Método seek.
#! Podemos controlar la posición desde la cual empezamos a leer.
# fichero = open('./ARCHIVOS_EXTERNOS/demo.txt', encoding='utf-8')
# fichero.seek(10)    #? Esta instruccion le dice a Python que lea el fichero desde la posicion 10
# print('Estamos leyendo desde el decimo caracter')
# print(fichero.read())
# fichero.close()


#! Apartado 6: lectura y escritura simultaneas.
# fichero = open('./ARCHIVOS_EXTERNOS/demo2.txt', 'r+', encoding='utf-8')
# lineas = fichero.readlines()
# print(lineas)

# fichero.write('\nEsta linea es mas nueva')
# fichero.close()


#! Apartado 7: Ejercicio resuelto
#! ENUNCIADO: Queremos comparar el tiempo que
#! tarda en sumar todos los elementos de una
#! lista un bucle for y un bucle while

#! Para ello, debemos calcular el tiempo empleado
#! en cada bucle varias veces y despues promediarlo.
#! Debemos cronometrar lo que tarda cada bucle cada 100 veces
#! y guardar cada resultado en un fichero.

import time, random

lista = []

for x in range(50000):
    lista.append(random.randint(0, 150000))
    
fichero = open('ARCHIVOS_EXTERNOS/times.txt', 'wt', encoding='utf-8')

for x in range(100):
    accFor = 0
    startTime = time.time()
    for num in lista:
        accFor += num
    elapsedTimeFor = time.time() - startTime
    
    #! Hacemos lo mismo pero para el while
    pos = 0
    accWhile = 0
    startTime = time.time()
    while pos < len(lista):
        accWhile += lista[pos]
        pos += 1
    elapsedTimeWhile = time.time() - startTime
    
    fichero.write(f'{elapsedTimeFor};{elapsedTimeWhile}\n')

fichero.close()

#! Calculando el promedio de tiempos
fichero = open('ARCHIVOS_EXTERNOS/times.txt', encoding='utf-8')

meanFor = 0
meanWhile = 0
samples = 0

for line in fichero.readlines():
    line.replace('\n', "")
    timeFor, timeWhile = line.split(';')
    meanFor += float(timeFor)
    meanWhile += float(timeWhile)
    samples += 1
    
print(f'Tiempo For: {(meanFor/samples) * (10 ** 3)}ms. Tiempo While: {(meanWhile/samples) * (10 ** 3)}ms')
fichero.close()


