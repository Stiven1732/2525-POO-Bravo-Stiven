import pickle

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario: clave = ID, valor = Producto

    def añadir_producto(self, producto):
        if producto.id in self.productos:
            print("❌ El producto ya existe.")
        else:
            self.productos[producto.id] = producto
            print("✅ Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("🗑️ Producto eliminado.")
        else:
            print("❌ Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        producto = self.productos.get(id_producto)
        if producto:
            if cantidad is not None:
                producto.actualizar_cantidad(cantidad)
            if precio is not None:
                producto.actualizar_precio(precio)
            print("🔄 Producto actualizado.")
        else:
            print("❌ Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        return encontrados

    def mostrar_todos(self):
        if not self.productos:
            print("📦 Inventario vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'wb') as f:
            pickle.dump(self.productos, f)
        print("💾 Inventario guardado.")

    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'rb') as f:
                self.productos = pickle.load(f)
            print("📂 Inventario cargado.")
        except FileNotFoundError:
            print("⚠️ Archivo no encontrado. Se iniciará un inventario vacío.")

# Menú interactivo
def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo("inventario.dat")

    while True:
        print("\n📋 MENÚ DE INVENTARIO")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("⚠️ Entrada inválida. Asegúrate de ingresar números válidos para cantidad y precio.")

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío si no aplica): ")
            precio = input("Nuevo precio (dejar vacío si no aplica): ")
            try:
                inventario.actualizar_producto(
                    id_producto,
                    cantidad=int(cantidad) if cantidad else None,
                    precio=float(precio) if precio else None
                )
            except ValueError:
                print("⚠️ Entrada inválida. Asegúrate de ingresar números válidos.")

        elif opcion == "4":
            nombre = input("Nombre del producto: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("🔍 No se encontraron productos con ese nombre.")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_en_archivo("inventario.dat")

        elif opcion == "7":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()