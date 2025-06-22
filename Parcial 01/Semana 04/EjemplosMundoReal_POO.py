class TiendaFinanzas:
    def __init__(self):
        self.ingresos = []  # Cada ingreso será un dict: {"descripcion": str, "monto": float}
        self.gastos = []    # Cada gasto será un dict: {"descripcion": str, "monto": float}

    def registrar_ingreso(self, descripcion, monto):
        self.ingresos.append({"descripcion": descripcion, "monto": monto})
        print(f"Ingreso registrado: {descripcion} - ${monto:.2f}")

    def registrar_gasto(self, descripcion, monto):
        self.gastos.append({"descripcion": descripcion, "monto": monto})
        print(f"Gasto registrado: {descripcion} - ${monto:.2f}")

    def mostrar_balance(self):
        total_ingresos = sum(i["monto"] for i in self.ingresos)
        total_gastos = sum(g["monto"] for g in self.gastos)
        saldo = total_ingresos - total_gastos

        print("\n======= BALANCE DE LA TIENDA =======")
        print(f"Total ingresos: ${total_ingresos:.2f}")
        print(f"Total gastos:   ${total_gastos:.2f}")
        print(f"Saldo neto:     ${saldo:.2f}")

    def mostrar_detalle(self):
        print("\n--- Ingresos ---")
        if not self.ingresos:
            print("No hay ingresos registrados.")
        else:
            for ingreso in self.ingresos:
                print(f"{ingreso['descripcion']} - ${ingreso['monto']:.2f}")

        print("\n--- Gastos ---")
        if not self.gastos:
            print("No hay gastos registrados.")
        else:
            for gasto in self.gastos:
                print(f"{gasto['descripcion']} - ${gasto['monto']:.2f}")


def menu():
    tienda = TiendaFinanzas()

    while True:
        print("\n===== SISTEMA DE FINANZAS TIENDA =====")
        print("1. Registrar venta (ingreso)")
        print("2. Registrar gasto")
        print("3. Ver balance")
        print("4. Ver detalle de ingresos y gastos")
        print("5. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            descripcion = input("Descripción de la venta: ")
            try:
                monto = float(input("Monto en $: "))
                tienda.registrar_ingreso(descripcion, monto)
            except ValueError:
                print("Monto inválido. Intente de nuevo.")
        elif opcion == "2":
            descripcion = input("Descripción del gasto: ")
            try:
                monto = float(input("Monto en $: "))
                tienda.registrar_gasto(descripcion, monto)
            except ValueError:
                print("Monto inválido. Intente de nuevo.")
        elif opcion == "3":
            tienda.mostrar_balance()
        elif opcion == "4":
            tienda.mostrar_detalle()
        elif opcion == "5":
            print("¡Gracias por usar el sistema de finanzas!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
