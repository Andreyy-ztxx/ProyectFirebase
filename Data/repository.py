from firebase_admin import db

class BibliotecaRepository:
    def __init__(self):
        self.libros_ref = db.reference("libros")
        self.estudiantes_ref = db.reference("estudiantes")

    def agregar_libro(self, libro):
        nuevo = self.libros_ref.push({"titulo": libro.titulo, "categoria": libro.categoria})
        return nuevo.key

    def listar_libros(self):
        datos = self.libros_ref.get() or {}
        return [{"id": k, "titulo": v.get("titulo", ""), "categoria": v.get("categoria", "")}
                for k, v in datos.items()]

    def agregar_estudiante(self, estudiante):
        nuevo = self.estudiantes_ref.push({"nombre": estudiante.nombre})
        return nuevo.key

    def listar_estudiantes(self):
        datos = self.estudiantes_ref.get() or {}
        return [{"id": k, "nombre": v.get("nombre", "")} for k, v in datos.items()]
