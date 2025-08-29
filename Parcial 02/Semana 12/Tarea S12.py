# ========================
# Clase Libro
# ========================
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Usamos tupla para los atributos inmutables
        self.datos = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    @property
    def titulo(self):
        return self.datos[0]

    @property
    def autor(self):
        return self.datos[1]

    def __str__(self):
        return f"{self.titulo} de {self.autor} [{self.categoria}] (ISBN: {self.isbn})"


# ========================
# Clase Usuario
# ========================
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


# ========================
# Clase Biblioteca
# ========================
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario: {ISBN: Libro}
        self.usuarios = {}  # Diccionario: {ID: Usuario}
        self.ids_usuarios = set()  # Conjunto para IDs únicos

    # ---------- Gestión de Libros ----------
    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print("⚠️ El libro ya existe en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"✅ Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"🗑️ Libro con ISBN {isbn} eliminado.")
        else:
            print("⚠️ No se encontró el libro con ese ISBN.")

    # ---------- Gestión de Usuarios ----------
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print("⚠️ Ya existe un usuario con ese ID.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"✅ Usuario registrado: {usuario}")

    def baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print(f"🗑️ Usuario con ID {id_usuario} dado de baja.")
        else:
            print("⚠️ No se encontró un usuario con ese ID.")

    # ---------- Préstamos ----------
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("⚠️ Usuario no encontrado.")
            return
        if isbn not in self.libros:
            print("⚠️ Libro no disponible en la biblioteca.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros.pop(isbn)  # El libro deja de estar disponible
        usuario.libros_prestados.append(libro)
        print(f"📚 Libro prestado: {libro} a {usuario.nombre}")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("⚠️ Usuario no encontrado.")
            return

        usuario = self.usuarios[id_usuario]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros[isbn] = libro  # Vuelve a estar disponible
                print(f"🔄 Libro devuelto: {libro}")
                return
        print("⚠️ Ese libro no estaba prestado a este usuario.")

    # ---------- Búsquedas ----------
    def buscar_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros.values() if libro.titulo.lower() == titulo.lower()]
        return resultados

    def buscar_por_autor(self, autor):
        resultados = [libro for libro in self.libros.values() if libro.autor.lower() == autor.lower()]
        return resultados

    def buscar_por_categoria(self, categoria):
        resultados = [libro for libro in self.libros.values() if libro.categoria.lower() == categoria.lower()]
        return resultados

    # ---------- Listar libros prestados ----------
    def listar_prestados_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"📖 Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(f" - {libro}")
            else:
                print(f"ℹ️ {usuario.nombre} no tiene libros prestados.")
        else:
            print("⚠️ Usuario no encontrado.")


# ========================
# Pruebas del Sistema
# ========================
if __name__ == "__main__":
    # Crear biblioteca
    biblio = Biblioteca()

    # Crear libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "1111")
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Fábula", "2222")
    libro3 = Libro("Don Quijote", "Miguel de Cervantes", "Clásico", "3333")

    # Agregar libros
    biblio.agregar_libro(libro1)
    biblio.agregar_libro(libro2)
    biblio.agregar_libro(libro3)

    # Crear usuarios
    usuario1 = Usuario("Ana", "U01")
    usuario2 = Usuario("Carlos", "U02")

    # Registrar usuarios
    biblio.registrar_usuario(usuario1)
    biblio.registrar_usuario(usuario2)

    # Prestar libros
    biblio.prestar_libro("U01", "1111")  # Ana toma Cien Años de Soledad
    biblio.prestar_libro("U02", "2222")  # Carlos toma El Principito

    # Listar libros prestados
    biblio.listar_prestados_usuario("U01")
    biblio.listar_prestados_usuario("U02")

    # Devolver libro
    biblio.devolver_libro("U01", "1111")
    biblio.listar_prestados_usuario("U01")

    # Buscar libros
    print("\n🔎 Búsqueda por autor 'Miguel de Cervantes':")
    for l in biblio.buscar_por_autor("Miguel de Cervantes"):
        print(l)
