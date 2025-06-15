class ClimaDia:
    """
    Clase que representa la información de un día del clima.
    """
    def _init_(self, numero_dia):
        self.__numero_dia = numero_dia
        self.__temperatura = 0.0

    def ingresar_temperatura(self):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {self.__numero_dia}: "))
                self.__temperatura = temp
                break
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número válido.")

    def obtener_temperatura(self):
        return self.__temperatura


class ClimaSemana:
    """
    Clase que gestiona el clima de una semana.
    """
    def _init_(self):
        self._dias = [ClimaDia(i + 1) for i in range(7)]  # Protegido en lugar de privado

    def ingresar_temperaturas(self):
        for dia in self._dias:
            dia.ingresar_temperatura()

    def calcular_promedio(self):
        if len(self._dias) == 0:
            return 0.0
        suma = sum(dia.obtener_temperatura() for dia in self._dias)
        promedio = suma / len(self._dias)
        return promedio


class ClimaSemanaConReporte(ClimaSemana):
    """
    Clase hija que añade un reporte detallado.
    """
    def mostrar_reporte(self):
        print("\n== Reporte de temperaturas de la semana ==")
        for idx, dia in enumerate(self._dias, start=1):
            print(f"Día {idx}: {dia.obtener_temperatura():.2f} grados")


def main():
    print("== Programa para calcular el promedio semanal del clima ==")
    semana = ClimaSemanaConReporte()
    semana.ingresar_temperaturas()
    promedio = semana.calcular_promedio()
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} grados.")
    semana.mostrar_reporte()


if __name__ == "__main__":
    main()