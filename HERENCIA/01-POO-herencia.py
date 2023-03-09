# Herencia Jerarquica

class Persona:
    
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        
    def presentarse(self):
        print(f'¡Hola! Me llamo {self.nombre} y tengo {self.edad} años.')
        

juan = Persona('Juan', 23, "3445765h")
juan.presentarse()
print(juan.dni)

# Definiendo la herencia
class Trabajador(Persona):
    
    def __init__(self, nombre, edad, dni, sueldo, cargo, empresa):
        super().__init__(nombre, edad, dni) # Parámetros que hereda del padre
        self.sueldo = sueldo
        self.cargo = cargo
        self.empresa = empresa
        
    def calcular_sueldo_anual(self):
        return 12 * self.sueldo + 2000
    

trabajador = Trabajador('Pedro', 45, "36548756h", 1500, "Desarrolador", "Google")
trabajador.presentarse()
print(trabajador.dni)
print(trabajador.calcular_sueldo_anual())


class Estudiante(Persona):
    
    def __init__(self, nombre, edad, dni, universidad, curso, asignaturas):
        super().__init__(nombre, edad, dni)
        self.universidad = universidad
        self.curso = curso
        self.asignaturas = asignaturas
    
    def describirse(self):
        print(f'''Hola, soy {self.nombre}, tengo {self.edad} años y estudio en la universidad {self.universidad}. Estoy en el curso {self.curso} y estoy viendo {self.asignaturas}''')

estudiante = Estudiante('Gabriel', 22, "46574875K", "Malaga", "Ing. Sistemas", ["Programación", "Cálculo", "Fisica"])
estudiante.describirse()
