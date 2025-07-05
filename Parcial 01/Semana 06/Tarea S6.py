# Clase base: Empleado
class Empleado:
    def __init__(self, nombre, salario):
        self._nombre = nombre  # atributo protegido (encapsulado)
        self._salario = salario  # atributo protegido (encapsulado)

    def descripcion(self):
        return f"Empleado: {self._nombre}, Salario: ${self._salario}"

    # Método para demostrar polimorfismo
    def calcular_bono(self):
        return self._salario * 0.10  # bono base del 10%


# Clase derivada: Gerente (hereda de Empleado)
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)  # llamada al constructor de la clase base
        self.departamento = departamento

    # Polimorfismo: sobrescritura del método calcular_bono
    def calcular_bono(self):
        return self._salario * 0.20  # bono especial del 20%

    # Método adicional
    def descripcion(self):
        return f"Gerente: {self._nombre}, Departamento: {self.departamento}, Salario: ${self._salario}"


# Clase derivada: Asistente (hereda de Empleado)
class Asistente(Empleado):
    def __init__(self, nombre, salario, horas_extra):
        super().__init__(nombre, salario)
        self.horas_extra = horas_extra

    def calcular_bono(self):
        return self.horas_extra * 5  # bono según horas extra trabajadas


# Crear instancias (objetos)
empleado1 = Empleado("Ana", 1200)
gerente1 = Gerente("Carlos", 2500, "Ventas")
asistente1 = Asistente("Lucía", 1000, 12)

# Imprimir descripciones y calcular bonos (polimorfismo en acción)
empleados = [empleado1, gerente1, asistente1]

for e in empleados:
    print(e.descripcion())
    print("Bono:", e.calcular_bono())
    print("-" * 40)
