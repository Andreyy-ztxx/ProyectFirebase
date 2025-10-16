def mostrar_menu():
    print("+========================================+")
    print("| Bienvenido a la Biblioteca (Firebase)  |")
    print("+========================================+")
    print("| 1. Registrar libro                     |")
    print("| 2. Registrar estudiante                |")
    print("| 3. Ver libros registrados              |")
    print("| 4. Ver estudiantes registrados         |")
    print("| 0. Salir                               |")
    print("+========================================+")

def loop_principal(vm):
    while True:
        mostrar_menu()
        opcion = input("| Ingrese el número de la opción: ")

        if opcion == "1":
            titulo = input("| Ingrese el título del libro: ")
            print("| Categorías:", ", ".join(vm.categorias))
            categoria = input("| Ingrese la categoría: ")
            ok, msg = vm.registrar_libro(titulo, categoria)
            imprimir_banner(msg, error=(not ok))

        elif opcion == "2":
            nombre = input("| Ingrese el nombre del estudiante: ")
            ok, msg = vm.registrar_estudiante(nombre)
            imprimir_banner(msg, error=(not ok))

        elif opcion == "3":
            libros = vm.obtener_libros()
            print("\n| Libros registrados:")
            if not libros:
                print("| No hay libros.")
            else:
                for l in libros:
                    print("| - [" + l["id"] + "] " + l["titulo"] + " (" + l["categoria"] + ")")

        elif opcion == "4":
            estudiantes = vm.obtener_estudiantes()
            print("\n| Estudiantes registrados:")
            if not estudiantes:
                print("| No hay estudiantes.")
            else:
                for e in estudiantes:
                    print("| - [" + e["id"] + "] " + e["nombre"])

        elif opcion == "0":
            print("----------------------------------------")
            print("| Saliendo del programa")
            print("----------------------------------------")
            break
        else:
            imprimir_banner("Opción inválida", error=True)

def imprimir_banner(mensaje, error=False):
    borde = "+" + "-" * 40 + "+"
    print(borde)
    if error:
        print("| ERROR: " + mensaje)
    else:
        print("| " + mensaje)
    print(borde)
