from gestor_usuarios import GestorUsuarios


def mostrar_menu():
    print("\n=== Gestión de Usuarios ===")
    print("1. Crear usuario")
    print("2. Listar usuarios")
    print("3. Modificar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")


def crear_usuario(gestor):
    print("\n--- Crear usuario ---")

    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    email = input("Email: ")
    password = input("Contraseña: ")

    correcto, mensaje = gestor.crear_usuario(nombre, apellidos, email, password)
    print(mensaje)


def listar_usuarios(gestor):
    print("\n--- Lista de usuarios ---")

    usuarios = gestor.listar_usuarios()

    if not usuarios:
        print("No hay usuarios registrados.")
        return

    for usuario in usuarios:
        print(f"ID: {usuario['id']}")
        print(f"Nombre: {usuario['nombre']} {usuario['apellidos']}")
        print(f"Email: {usuario['email']}")
        print("-" * 30)


def modificar_usuario(gestor):
    print("\n--- Modificar usuario ---")

    try:
        id_usuario = int(input("ID del usuario a modificar: "))
    except ValueError:
        print("El ID debe ser un número.")
        return

    nombre = input("Nuevo nombre: ")
    apellidos = input("Nuevos apellidos: ")
    email = input("Nuevo email: ")

    correcto, mensaje = gestor.modificar_usuario(
        id_usuario,
        nombre,
        apellidos,
        email
    )

    print(mensaje)


def eliminar_usuario(gestor):
    print("\n--- Eliminar usuario ---")

    try:
        id_usuario = int(input("ID del usuario a eliminar: "))
    except ValueError:
        print("El ID debe ser un número.")
        return

    correcto, mensaje = gestor.eliminar_usuario(id_usuario)
    print(mensaje)


def main():
    gestor = GestorUsuarios()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_usuario(gestor)
        elif opcion == "2":
            listar_usuarios(gestor)
        elif opcion == "3":
            modificar_usuario(gestor)
        elif opcion == "4":
            eliminar_usuario(gestor)
        elif opcion == "5":
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()