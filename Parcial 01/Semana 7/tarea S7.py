class ProductoLimpieza:
    """
    Clase que representa un producto de limpieza en 'La Casa Limpia'.
    Demuestra uso de constructor y destructor para inicializar y cerrar recursos.
    """

    def __init__(self, nombre, categoria, precio, stock):
        """
        Constructor: se ejecuta al crear el objeto.
        Inicializa atributos y muestra mensaje de registro.
        """
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        print(f"Producto registrado: {self.nombre} ({self.categoria}) - ${self.precio} | Stock: {self.stock}")

    def mostrar_info(self):
        """Método para mostrar detalles del producto."""
        print(f"🧴 {self.nombre} - Categoría: {self.categoria} - Precio: ${self.precio} - Stock disponible: {self.stock}")

    def actualizar_stock(self, cantidad):
        """Actualiza el stock (agregando o reduciendo)."""
        self.stock += cantidad
        print(f"Nuevo stock de '{self.nombre}': {self.stock}")

    def __del__(self):
        """
        Destructor: se llama cuando el objeto es destruido.
        Ideal para liberar recursos como conexiones, memoria o simplemente notificar limpieza.
        """
        print(f"Producto '{self.nombre}' eliminado del sistema.")

# 🧼 Ejemplo de uso:
if __name__ == "__main__":
    desinfectante = ProductoLimpieza("Desinfectante Multiusos", "Superficies", 4.99, 50)
    desinfectante.mostrar_info()
    desinfectante.actualizar_stock(-5)

    # Cuando finaliza el programa o se elimina el objeto, el destructor se activa automáticamente