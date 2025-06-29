import math

def calcular_area_circulo(radio: float) -> float:
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio: float) -> float:
    return 2 * math.pi * radio

def calcular_area_rectangulo(base: float, altura: float) -> float:
    return base * altura

def calcular_perimetro_rectangulo(base: float, altura: float) -> float:
    return 2 * (base + altura)

def mostrar_resultados(figura: str, area: float, perimetro: float):
    print(f"\nResultados para el {figura}:")
    print(f"Área: {area:.2f}")
    print(f"Perímetro: {perimetro:.2f}")

def main():
    print("=== Calculadora de Figuras Geométricas ===")
    print("Opciones disponibles:")
    print("1. Círculo")
    print("2. Rectángulo")

    opcion = input("Elige una figura (1 o 2): ")

    es_valida = opcion == "1" or opcion == "2"

    if not es_valida:
        print("Opción no válida. Finalizando el programa.")
        return

    if opcion == "1":
        radio = float(input("Introduce el radio del círculo: "))
        area = calcular_area_circulo(radio)
        perimetro = calcular_perimetro_circulo(radio)
        mostrar_resultados("círculo", area, perimetro)

    elif opcion == "2":
        base = float(input("Introduce la base del rectángulo: "))
        altura = float(input("Introduce la altura del rectángulo: "))
        area = calcular_area_rectangulo(base, altura)
        perimetro = calcular_perimetro_rectangulo(base, altura)
        mostrar_resultados("rectángulo", area, perimetro)

if __name__ == "__main__":
    main()
