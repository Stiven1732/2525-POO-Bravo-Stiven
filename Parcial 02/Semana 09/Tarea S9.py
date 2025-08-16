class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        # Verificar que el ID no se repita
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Error: El ID ya existe en el inventario.")
                return
        self.productos.append(producto)
        print("✅ Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("🗑 Producto eliminado con éxito.")
                return
        print("❌ Error: No se encontró el producto con ese ID.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("🔄 Producto actualizado con éxito.")
                return
        print("❌ Error: No se encontró el producto con ese ID.")

    def buscar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            print("🔎 Productos encontrados:")
            for p in encontrados:
                print(p)
        else:
            print("❌ No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print("📦 Inventario vacío.")
        else:
            print("📋 Inventario actual:")
            for p in self.productos:
                print(p)


def menu():
    inventario = Inventario()
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID: ").strip()
            nombre = input("Ingrese nombre: ").strip()

            # Manejo de errores para cantidad y precio
            try:
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
            except ValueError:
                print("❌ Error: La cantidad debe ser un número entero y el precio un número decimal.")
                continue

            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ").strip()
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ").strip()
            cantidad_input = input("Nueva cantidad (dejar vacío si no cambia): ").strip()
            precio_input = input("Nuevo precio (dejar vacío si no cambia): ").strip()

            cantidad = int(cantidad_input) if cantidad_input else None
            precio = float(precio_input) if precio_input else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ").strip()
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("👋 Saliendo del sistema. ¡Hasta pronto!")
            break

        else:
            print("❌ Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
