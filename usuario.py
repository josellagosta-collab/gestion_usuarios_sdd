"""Modelo simple `Usuario`.

Este módulo define una representación mínima de usuario y un método
para convertir la instancia a un diccionario serializable en JSON.

Nota didáctica: en aplicaciones reales la entidad Usuario normalmente
llevaría más métodos y no almacenaría contraseñas en texto plano.
"""

from typing import Dict


class Usuario:
    """Representa un usuario del sistema.

    Atributos públicos:
    - `id`: identificador numérico del usuario.
    - `nombre`, `apellidos`, `email`, `password`.
    """

    def __init__(self, id: int, nombre: str, apellidos: str, email: str, password: str) -> None:
        self.id: int = id
        self.nombre: str = nombre
        self.apellidos: str = apellidos
        self.email: str = email
        self.password: str = password

    def convertir_a_diccionario(self) -> Dict[str, object]:
        """Devuelve una representación en diccionario lista para JSON.

        Mantiene las claves esperadas por el resto del código.
        """
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "email": self.email,
            "password": self.password,
        }