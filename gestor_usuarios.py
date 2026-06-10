"""Gestión de usuarios.

Este módulo implementa las operaciones básicas (CRUD) sobre una colección
de usuarios almacenada en un archivo JSON. Los comentarios y docstrings
explican las reglas de negocio y el contrato de cada método para fines
didácticos y de mantenimiento.
"""

import re
from typing import Dict, List, Optional, Tuple

from repositorio_usuarios import cargar_usuarios, guardar_usuarios
from usuario import Usuario


class GestorUsuarios:
    """Clase encargada de la lógica de negocio para usuarios.

    - Mantiene una lista en memoria (`self.usuarios`) con diccionarios que
      representan usuarios.
    - Persiste la lista en `archivo` en formato JSON.
    - No gestiona concurrencia; para usos multi-proceso se deberá añadir
      un mecanismo de bloqueo externo.
    """

    def __init__(self, archivo: str = "usuarios.json") -> None:
        """Inicializa el gestor y carga los usuarios desde disco.

        Args:
            archivo: Ruta al archivo JSON que contiene la lista de usuarios.
        """
        self.archivo: str = archivo
        self.usuarios: List[Dict[str, object]] = []
        self.cargar_usuarios()

    def cargar_usuarios(self) -> None:
        """Carga la lista de usuarios desde `self.archivo`.

        Si el archivo no existe, inicializa una lista vacía. Si el JSON está
        corrupto o no se puede leer, se recupera con una lista vacía para
        evitar excepciones que rompan la aplicación de consola.
        """
        self.usuarios = cargar_usuarios(self.archivo)

        for usuario in self.usuarios:
            # Aceptamos datos legacy con `password` sin `salt`.
            if "salt" not in usuario:
                usuario["salt"] = ""

    def guardar_usuarios(self) -> None:
        """Persiste la lista de usuarios en `self.archivo` de forma atómica."""
        guardar_usuarios(self.archivo, self.usuarios)

    def obtener_siguiente_id(self) -> int:
        """Devuelve el siguiente ID entero disponible para un nuevo usuario.

        Se basa en el mayor `id` actualmente almacenado + 1. Si la lista está
        vacía, devuelve 1.
        """
        if not self.usuarios:
            return 1
        return max(usuario["id"] for usuario in self.usuarios) + 1

    def email_existe(self, email: str) -> bool:
        """Comprueba si un `email` ya está registrado.

        Devuelve `True` si existe al menos un usuario con ese email, `False`
        en caso contrario.
        """
        return any(
            usuario["email"].lower() == email.lower() for usuario in self.usuarios
        )

    def email_valido(self, email: str) -> bool:
        """Valida el formato básico de un email.

        Esta validación es simple y cubre los casos más comunes. En un
        proyecto más grande, conviene usar una librería dedicada.
        """
        return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email))

    def crear_usuario(
        self, nombre: str, apellidos: str, email: str, password: str
    ) -> Tuple[bool, str]:
        """Crea un nuevo usuario si cumple las reglas de negocio.

        Reglas principales validadas aquí:
        - `nombre` y `email` son obligatorios.
        - `email` debe ser único.
        - `password` debe tener al menos 8 caracteres.

        Devuelve una tupla `(ok, mensaje)` donde `ok` es `True` en caso de
        éxito y `False` en caso de fallo con un mensaje humano-legible.
        """
        if not nombre.strip():
            return False, "El nombre es obligatorio."

        if not email.strip():
            return False, "El email es obligatorio."

        if not self.email_valido(email):
            return False, "El email no tiene un formato válido."

        if self.email_existe(email):
            return False, "Ya existe un usuario con ese email."

        if len(password) < 8:
            return False, "La contraseña debe tener al menos 8 caracteres."

        nuevo_usuario = Usuario.crear_con_password(
            self.obtener_siguiente_id(),
            nombre,
            apellidos,
            email,
            password,
        )

        # Guardamos la representación en diccionario del usuario.
        self.usuarios.append(nuevo_usuario.convertir_a_diccionario())
        self.guardar_usuarios()

        return True, "Usuario creado correctamente."

    def listar_usuarios(self) -> List[Dict[str, object]]:
        """Devuelve la lista de usuarios actualmente cargada en memoria."""
        return self.usuarios

    def buscar_usuario_por_id(self, id_usuario: int) -> Optional[Dict[str, object]]:
        """Busca y devuelve un usuario por su `id`.

        Devuelve `None` si no existe.
        """
        for usuario in self.usuarios:
            if usuario["id"] == id_usuario:
                return usuario
        return None

    def modificar_usuario(
        self, id_usuario: int, nombre: str, apellidos: str, email: str
    ) -> Tuple[bool, str]:
        """Modifica los datos de un usuario existente.

        Validaciones:
        - El usuario debe existir.
        - `nombre` y `email` son obligatorios.
        - No se permite duplicar `email` entre usuarios distintos.
        """
        usuario = self.buscar_usuario_por_id(id_usuario)

        if usuario is None:
            return False, "No existe un usuario con ese ID."

        if not nombre.strip():
            return False, "El nombre es obligatorio."

        if not email.strip():
            return False, "El email es obligatorio."

        if not self.email_valido(email):
            return False, "El email no tiene un formato válido."

        for otro_usuario in self.usuarios:
            if (
                otro_usuario["email"].lower() == email.lower()
                and otro_usuario["id"] != id_usuario
            ):
                return False, "Ya existe otro usuario con ese email."

        usuario["nombre"] = nombre
        usuario["apellidos"] = apellidos
        usuario["email"] = email

        self.guardar_usuarios()

        return True, "Usuario modificado correctamente."

    def eliminar_usuario(self, id_usuario: int) -> Tuple[bool, str]:
        """Elimina un usuario por `id` si existe.

        Devuelve `(True, mensaje)` si la eliminación fue satisfactoria, o
        `(False, mensaje)` si no existe el usuario.
        """
        usuario = self.buscar_usuario_por_id(id_usuario)

        if usuario is None:
            return False, "No existe un usuario con ese ID."

        self.usuarios.remove(usuario)
        self.guardar_usuarios()

        return True, "Usuario eliminado correctamente."
