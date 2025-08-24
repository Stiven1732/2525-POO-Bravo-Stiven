import os

class Producto:
    def __init__(self, codigo, nombre, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.codigo},{self.nombre},{self.cantidad}"

    @staticmethod
    def desde_linea(linea):
        partes = linea.strip().split(",")
        if len(partes) == 3:
            return Producto(partes[0], partes[1], int(partes[2]))
        return None

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = {}
        self.archivo = archivo
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    producto = Producto.desde_linea(linea)
                    if producto:
                        self.productos[producto.codigo] = producto
            print("✅ Inventario cargado correctamente.")
        except FileNotFoundError:
            print("⚠️ Archivo no encontrado. Se creará uno nuevo al guardar.")
        except PermissionError:
            print("❌ Permiso denegado para leer el archivo.")
        except Exception as e:
            print(f"❌ Error inesperado al leer el archivo: {e}")

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos.values():
                    f.write(str(producto) + "\n")
            print("✅ Inventario guardado exitosamente.")
        except PermissionError:
            print("❌ Permiso denegado para escribir en el archivo.")
        except Exception as e:
            print(f"❌ Error inesperado al guardar el archivo: {e}")

    def agregar_producto(self, codigo, nombre, cantidad):
        if codigo in self.productos:
            print("⚠️ El producto ya existe.")
        else:
            self.productos[codigo] = Producto(codigo, nombre, cantidad)
            self.guardar_en_archivo()
            print("✅ Producto agregado correctamente.")

    def actualizar_producto(self, codigo, cantidad):
        if codigo in self.productos:
            self.productos[codigo].cantidad = cantidad
            self.guardar_en_archivo()
            print("✅ Producto actualizado correctamente.")
        else:
            print("❌ Producto no encontrado.")

    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            self.guardar_en_archivo()
            print("✅ Producto eliminado correctamente.")
        else:
            print("❌ Producto no encontrado.")

    def mostrar_inventario(self):
        if not self.productos:
            print("📦 Inventario vacío.")
        else:
            print("📋 Inventario actual:")
            for producto in self.productos.values():
                print(f" - {producto.codigo}: {producto.nombre} ({producto.cantidad})")

# Interfaz de usuario
def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Mostrar inventario")
        print("2. Agregar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            inventario.mostrar_inventario()
        elif opcion == "2":
            codigo = input("Código del producto: ")
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
                inventario.agregar_producto(codigo, nombre, cantidad)
            except ValueError:
                print("❌ Cantidad inválida.")
        elif opcion == "3":
            codigo = input("Código del producto a actualizar: ")
            try:
                cantidad = int(input("Nueva cantidad: "))
                inventario.actualizar_producto(codigo, cantidad)
            except ValueError:
                print("❌ Cantidad inválida.")
        elif opcion == "4":
            codigo = input("Código del producto a eliminar: ")
            inventario.eliminar_producto(codigo)
        elif opcion == "5":
            print("👋 Saliendo del programa.")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    menu()