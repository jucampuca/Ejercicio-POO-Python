# CLASES ABSTRACTAS:
#     - NO LAS VAMOS A INSTANCIAR NUNCA DIRECTAMENTE.
#     - CONTIENEN POR LO MENOS UN METODO ABSTRACTO
#     - LAS VAMOS A USAR DE BASE PARA SUBCLASES MAS ESPECIFICAS

# METODOS ABSTRACTOS:
#     - DEBEMOS SOBREESCRIBIRLOS EN CADA UNA DE LAS SUBCLASES

from abc import ABC, abstractmethod

class Personaje(ABC):
    
    @abstractmethod # Con este decorador estamos convirtiendo nuestro método en un método abstracto
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 0
        self.inventario = []
        self.vida = 100
        
    @abstractmethod
    def atacar(self, objetivo):
        pass    # Al usar el método pass, estamos asegurando que el método atacar se deba sobreescribir
    
    @abstractmethod
    def getStatus(self):
        print(f'Nombre: {self.nombre}. Nivel: {self.nivel}')
    
    def subirDeNivel(self):
        self.nivel += 1
        
    def verInventario(self):
        print(f'Inventario de {self.nombre}')
        for objeto in self.inventario:
            print(objeto)
            
    
# Creamos la primera clase que va a heredar de personaje
class Mago(Personaje):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 120
        self.inteligencia = 95
        self.inventario = ["Poción de Maná", "Grimorio"]
        
    # Sobreescribiendo los métodos abstractos
    def getStatus(self):
        print(f'Clase Mago')
        super().getStatus()
        
    def atacar(self, objetivo):
        objetivo.vida -= self.inteligencia * 0.6
        print(f'Actualmente el objetivo tiene {objetivo.vida} puntos de vida')
        

class Guerrero(Personaje):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 200
        self.fuerza = 75
        self.inventario = ["Poción de vida", "Escudo", "Espada"]
        
    def getStatus(self):
        print(f'Clase guerrero')
        super().getStatus()
        
    def atacar(self, objetivo):
        objetivo.vida -= self.fuerza * 0.8
        print(f'Actualmente el objetivo tiene {objetivo.vida} puntos de vida')


guerrero = Guerrero("Kaladin")
mago = Mago("Juno")

guerrero.getStatus()
mago.getStatus()

guerrero.verInventario()
mago.verInventario()

mago.atacar(guerrero)
guerrero.atacar(mago)

  


