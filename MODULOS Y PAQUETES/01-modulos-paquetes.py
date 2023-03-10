# MODULOS Y PAQUETES

#! Apartado 1: Módulos
#! Los módulos son archivos de Python que pueden contener funciones, clases y variables.
#! Podemos importarlas a nuestros archivos para hacer uso de estas
#! sin tener que volver a escribir su código.

# import calcular_area

# from calcular_area import areaCirculo, areaCuadrado, areaTriengulo#
# from calcular_area import *

# print(areaCirculo(4))
# print(areaCuadrado(7))
# print(areaTriengulo(2, 4))

#! Los paquetes son conjuntos de módulos relacionados entre sí en un mismo directorio
from geometria.calcularPerimetro import CalculaPerimetros as CP
from geometria.calcularArea import areaCirculo as ac

cp = CP()
print(cp.perimetroCirculo(2))


