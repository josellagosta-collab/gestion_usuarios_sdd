"""Interfaz de consola para la aplicación de gestión de usuarios.

Este módulo ofrece una CLI basada en `argparse` y un modo interactivo
opcionales. La lógica de negocio permanece en `GestorUsuarios`.
"""

import argparse
import logging
from typing import List

from gestor_usuarios import GestorUsuarios


def configurar_logging() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def crear_usuario(gestor: GestorUsuarios, nombre: str, apellidos: str, email: str, password: str) -> int:
    correcto, mensaje = gestor.crear_usuario(nombre, apellidos, email, password)
    if correcto:
        logging.info(mensaje)
        return 0
    logging.error(mensaje)
    return 1


def listar_usuarios(gestor: GestorUsuarios) -> int:
    usuarios = gestor.listar_usuarios()
    if not usuarios:
        logging.info("No hay usuarios registrados.")
        return 0

    for usuario in usuarios:
        logging.info("ID: %s", usuario["id"])
        logging.info("Nombre: %s %s", usuario["nombre"], usuario["apellidos"])
        logging.info("Email: %s", usuario["email"])
        logging.info("%s", "-" * 30)
    return 0


def modificar_usuario(gestor: GestorUsuarios, id_usuario: int, nombre: str, apellidos: str, email: str) -> int:
    correcto, mensaje = gestor.modificar_usuario(id_usuario, nombre, apellidos, email)
    if correcto:
        logging.info(mensaje)
        return 0
    logging.error(mensaje)
    return 1


def eliminar_usuario(gestor: GestorUsuarios, id_usuario: int) -> int:
    correcto, mensaje = gestor.eliminar_usuario(id_usuario)
    if correcto:
        logging.info(mensaje)
        return 0
    logging.error(mensaje)
    return 1


def ejecutar_interactivo(gestor: GestorUsuarios) -> int:
    while True:
        print("\n=== Gestión de Usuarios ===")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Modificar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellidos = input("Apellidos: ")
            email = input("Email: ")
            password = input("Contraseña: ")
            crear_usuario(gestor, nombre, apellidos, email, password)
        elif opcion == "2":
            listar_usuarios(gestor)
        elif opcion == "3":
            try:
                id_usuario = int(input("ID del usuario a modificar: "))
            except ValueError:
                print("El ID debe ser un número.")
                continue
            nombre = input("Nuevo nombre: ")
            apellidos = input("Nuevos apellidos: ")
            email = input("Nuevo email: ")
            modificar_usuario(gestor, id_usuario, nombre, apellidos, email)
        elif opcion == "4":
            try:
                id_usuario = int(input("ID del usuario a eliminar: "))
            except ValueError:
                print("El ID debe ser un número.")
                continue
            eliminar_usuario(gestor, id_usuario)
        elif opcion == "5":
            print("Saliendo de la aplicación...")
            return 0
        else:
            print("Opción no válida.")


def main(argv: List[str] | None = None) -> int:
    configurar_logging()

    parser = argparse.ArgumentParser(
        description="Gestión de usuarios desde la línea de comandos.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--archivo", default="usuarios.json", help="Archivo JSON donde se guardan los usuarios.")

    subparsers = parser.add_subparsers(dest="comando", title="comandos")

    parser_crear = subparsers.add_parser("crear", help="Crear un nuevo usuario")
    parser_crear.add_argument("--nombre", required=True, help="Nombre del usuario")
    parser_crear.add_argument("--apellidos", required=True, help="Apellidos del usuario")
    parser_crear.add_argument("--email", required=True, help="Email del usuario")
    parser_crear.add_argument("--password", required=True, help="Contraseña del usuario")

    parser_listar = subparsers.add_parser("listar", help="Listar todos los usuarios")

    parser_modificar = subparsers.add_parser("modificar", help="Modificar un usuario existente")
    parser_modificar.add_argument("--id", type=int, required=True, help="ID del usuario")
    parser_modificar.add_argument("--nombre", required=True, help="Nuevo nombre")
    parser_modificar.add_argument("--apellidos", required=True, help="Nuevos apellidos")
    parser_modificar.add_argument("--email", required=True, help="Nuevo email")

    parser_eliminar = subparsers.add_parser("eliminar", help="Eliminar un usuario")
    parser_eliminar.add_argument("--id", type=int, required=True, help="ID del usuario a eliminar")

    subparsers.add_parser("interactivo", help="Modo interactivo en consola")

    args = parser.parse_args(argv)
    gestor = GestorUsuarios(args.archivo)

    if args.comando is None or args.comando == "interactivo":
        return ejecutar_interactivo(gestor)
    if args.comando == "crear":
        return crear_usuario(gestor, args.nombre, args.apellidos, args.email, args.password)
    if args.comando == "listar":
        return listar_usuarios(gestor)
    if args.comando == "modificar":
        return modificar_usuario(gestor, args.id, args.nombre, args.apellidos, args.email)
    if args.comando == "eliminar":
        return eliminar_usuario(gestor, args.id)

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
