from Domain.models import Libro, Estudiante

class BibliotecaViewModel:
    def __init__(self, repository):
        self.repository = repository
        self.categorias = ["Ciencia", "Literatura", "Historia"]

    def registrar_libro(self, titulo, categoria):
        if categoria not in self.categorias:
            return False, "Categoría no válida. Use: " + ", ".join(self.categorias)
        if not titulo.strip():
            return False, "El título no puede estar vacío."
        libro = Libro(titulo.strip(), categoria)
        libro_id = self.repository.agregar_libro(libro)
        return True, "Libro '" + titulo + "' registrado (ID: " + libro_id + ")."

    def registrar_estudiante(self, nombre):
        if not nombre.strip():
            return False, "El nombre no puede estar vacío."
        est = Estudiante(nombre.strip())
        est_id = self.repository.agregar_estudiante(est)
        return True, "Estudiante '" + nombre + "' registrado (ID: " + est_id + ")."

    def obtener_libros(self):
        return self.repository.listar_libros()

    def obtener_estudiantes(self):
        return self.repository.listar_estudiantes()
