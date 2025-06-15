def ingresar_temperaturas(dias):
    """
    Función para ingresar las temperaturas de cada día.
    :param dias: Número de días a solicitar (int)
    :return: Lista de temperaturas ingresadas (list of float)
    """
    temperaturas = []
    for i in range(1, dias + 1):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {i}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número válido.")
    return temperaturas


def calcular_promedio_semanal(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    :param temperaturas: Lista de temperaturas (list of float)
    :return: Promedio de las temperaturas (float)
    """
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio


def main():
    DIAS_SEMANA = 7
    print("== Programa para calcular el promedio semanal de temperatura ==")
    temperaturas = ingresar_temperaturas(DIAS_SEMANA)
    promedio = calcular_promedio_semanal(temperaturas)
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} grados.")


if __name__ == "__main__":
    main()