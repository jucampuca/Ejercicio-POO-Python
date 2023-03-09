from Concursante import Concursante
import time

class Soltero(Concursante):
    
    def __init__(self, nombre, edad, profesion, procedencia):
        super().__init__(nombre, edad, profesion, procedencia)
        self._ligues = []
        
    #! Definimos el método str para los print que hacemos de la clase Soltero
    def __str__(self):
        return f'\n{self._nombre} ha venido a enamorarse a la Isla de las Tentaciones. Tiene {self._edad}, viene de {self._procedencia} y su trabajo es {self._profesion}\n'
        
        
    def addLigue(self, tentado):
        self._ligues.append(tentado)
        
    def ligarCon(self, tentado):
        self.addLigue(tentado)
        print(f'{self._nombre} ha conectado completamente con {tentado._nombre}. Esta es su {len(self._ligues)} a conquistar')
        
        #! Colocamos una funcion para detener la ejecución por 1 segundo
        time.sleep(1)
        
        #! Vamos a sobreescribir el método hablar
        def hablar(self, mensaje):
            target = " "
            if len(self._ligues) > 0:
                target = f' (que ha conquistado a {self._ligues[-1]._nombre}) '
            print(f'\n[{self._nombre.upper()}]{target}: {mensaje}\n')
            time.sleep(1)
        
     
        
        