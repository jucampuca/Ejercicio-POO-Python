# Encapsulamiento

class Circulo:
    
    def __init__(self, radio):
        self.__radio = radio
        self.__pi = 3.1416
        
    def calcularPerimetro(self):
        return 2 * self.__pi * self.__radio
    
    def calcularArea(self):
        return self.__pi * self.__radio**2

    # Crearemos un método publico para acceder a pi ya que es privado
    def getPI(self):
        return self.__pi
    
    def setRadio(self, nuevoValor):
        if type(nuevoValor) == int or type(nuevoValor) == float:
            if nuevoValor >= 0:
                self.__radio = nuevoValor
                print(f'El radio se ha modificado correcta,mente: {self.__radio}')
            else:
                print("El radio no puede ser negativo")
        else:
            print("El radio tiene que ser un numero positivo")

    
circulo = Circulo(2.5)
print(f'El área del circulo es: {circulo.calcularArea()}')
print(f'El perímetro del circulo es: {circulo.calcularPerimetro()}')
print(f'La constante PI es {circulo.getPI()}')

# Modificamos el radio
circulo.setRadio(34)
circulo.setRadio(-23)
circulo.setRadio("Hola que tal")


       
# atributo: __radio -> _Circulo__radop => En general _NombreDeLaClase__NombreDelAtributo
# En este caso, el encapsulamiento no existe. Python lo que hace es cambiar el nombre por lo que
# tenemos en la nomenclatura del codigo de arriba.

