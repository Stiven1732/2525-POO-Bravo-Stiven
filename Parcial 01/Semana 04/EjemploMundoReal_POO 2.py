class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} - Stock: {self.stock}"


class Tienda:
    def __init__(self):
        self.productos = []
        self.total_ventas = 0.0

    def agregar_producto(self, nombre, precio, stock):
        nuevo = Producto(nombre, precio, stock)
        self.productos.append(nuevo)
        print(f"Producto '{nombre}' agregado con éxito.")

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en la tienda.")
        else:
            print("\nListado de productos:")
            for idx, prod in enumerate(self.productos, 1):
                print(f"{idx}. {prod}")

    def vender_producto(self, nombre, cantidad):
        for prod in self.productos:
            if prod.nombre.lower() == nombre.lower():
                if prod.stock >= cantidad:
                    total = prod.precio * cantidad
                    prod.stock -= cantidad
                    self.total_ventas += total
                    print(f"Venta realizada: {cantidad} x {prod.nombre} = ${total:.2f}")
                    return
                else:
                    print(f"Stock insuficiente. Stock disponible: {prod.stock}")
                    return
        print(f"Producto '{nombre}' no encontrado.")

    def mostrar_total_ventas(self):
        print(f"\nTotal vendido: ${self.total_ventas:.2f}")


def menu():
    tienda = Tienda()

    while True:
        print("\n===== TIENDA MINORISTA ECUADOR =====")
        print("1. Agregar producto")
        print("2. Ver productos")
        print("3. Vender producto")
        print("4. Ver total de ventas")
        print("5. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            try:
                precio = float(input("Precio en $: "))
                stock = int(input("Cantidad en stock: "))
                tienda.agregar_producto(nombre, precio, stock)
            except ValueError:
                print("Datos inválidos. Intente nuevamente.")
        elif opcion == "2":
            tienda.mostrar_productos()
        elif opcion == "3":
            nombre = input("Nombre del producto a vender: ")
            try:
                cantidad = int(input("Cantidad: "))
                tienda.vender_producto(nombre, cantidad)
            except ValueError:
                print("Cantidad inválida.")
        elif opcion == "4":
            tienda.mostrar_total_ventas()
        elif opcion == "5":
            print("¡Gracias por usar el sistema de la tienda!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
