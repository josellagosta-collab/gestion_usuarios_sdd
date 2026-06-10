"""Modelo de usuario con almacenamiento seguro de contraseñas.

Este módulo define una representación de usuario que guarda el hash de la
contraseña junto a una sal para evitar almacenar datos sensibles en texto
plano. En aplicaciones más completas, esta lógica se integraría con una
capa de autenticación dedicada.
"""

import base64
import hashlib
import os
from typing import Dict


class Usuario:
    """Representa un usuario en el sistema.

    Este modelo mantiene un hash de contraseña en lugar de la contraseña
    original en texto plano.
    """

    def __init__(
        self, id: int, nombre: str, apellidos: str, email: str, password: str, salt: str
    ) -> None:
        self.id: int = id
        self.nombre: str = nombre
        self.apellidos: str = apellidos
        self.email: str = email
        self.password: str = password
        self.salt: str = salt

    @classmethod
    def crear_con_password(
        cls, id: int, nombre: str, apellidos: str, email: str, password: str
    ) -> "Usuario":
        """Crea una instancia de usuario usando un hash seguro de la contraseña."""
        salt = base64.b64encode(os.urandom(16)).decode("utf-8")
        password_hash = cls._hash_password(password, salt)
        return cls(id, nombre, apellidos, email, password_hash, salt)

    @staticmethod
    def _hash_password(password: str, salt: str) -> str:
        """Genera un hash PBKDF2-HMAC-SHA256 con la sal proporcionada."""
        raw_salt = base64.b64decode(salt.encode("utf-8"))
        dk = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            raw_salt,
            200_000,
        )
        return base64.b64encode(dk).decode("utf-8")

    def verificar_password(self, password: str) -> bool:
        """Comprueba si una contraseña en claro coincide con el hash guardado."""
        if not self.salt:
            return False
        return self.password == self._hash_password(password, self.salt)

    def convertir_a_diccionario(self) -> Dict[str, object]:
        """Devuelve la representación serializable del usuario."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "email": self.email,
            "password": self.password,
            "salt": self.salt,
        }
