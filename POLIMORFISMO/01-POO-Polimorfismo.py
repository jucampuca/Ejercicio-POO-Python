# Polimorfismo
# Podemos redefinir métodos que heredamos de la clase padre

class Empleado:
    
    def __init__(self, nombre, sueldoMensual):
        self.nombre = nombre
        self.sueldoMensual = sueldoMensual
        
    def calcularSueldoAnual(self):
        sueldo = 12 * self.sueldoMensual * (1 + 1/100)
        print(f'El sueldo anual de {self.nombre}, empleado normal, es de ${sueldo}')
    
class Contable(Empleado):
    
    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)
        
    # Usando el polimorfismo
    def calcularSueldoAnual(self):
        sueldo = 12 * self.sueldoMensual * (1 + 4/100)
        print(f'El sueldo anual de {self.nombre}, contable es de ${sueldo}')
        
class Publicista(Empleado):
    
    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)
    
    # Usando el polimorfismo
    def calcularSueldoAnual(self):
        sueldo = 12 * self.sueldoMensual * (1 + 5/100)
        print(f'El sueldo anual de {self.nombre}, publicista es de ${sueldo}')
    
class Becario(Empleado):
    
    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)
    
    def calcularSueldoAnual(self):
        sueldo = 12 * self.sueldoMensual
        print(f'El sueldo anual de {self.nombre}, becario es de ${sueldo}')
        

empleados = [
    Empleado('Juan', 1000),
    Contable('Angela', 1200),
    Publicista('Ryan', 1500),
    Becario('Pedro', 800)
]

for empleado in empleados:
    empleado.calcularSueldoAnual()

    