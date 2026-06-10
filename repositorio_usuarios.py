import json
import os
import tempfile
from typing import Any, Dict, List


def cargar_usuarios(archivo: str) -> List[Dict[str, Any]]:
    """Carga usuarios desde un archivo JSON.

    Devuelve una lista vacía si el archivo no existe, está corrupto o no se
    puede leer.
    """
    if not os.path.exists(archivo):
        return []

    try:
        with open(archivo, "r", encoding="utf-8") as f:
            usuarios = json.load(f)
        if isinstance(usuarios, list):
            return usuarios
    except (json.JSONDecodeError, OSError):
        pass

    return []


def guardar_usuarios(archivo: str, usuarios: List[Dict[str, Any]]) -> None:
    """Guarda usuarios en JSON de forma atómica.

    Se escribe primero en un archivo temporal dentro del mismo directorio y
    luego se sustituye el archivo original con `os.replace` para minimizar
    la posibilidad de corrupción de datos.
    """
    directorio = os.path.dirname(os.path.abspath(archivo)) or "."
    fd, temp_path = tempfile.mkstemp(prefix=".tmp_", suffix=".json", dir=directorio)

    try:
        with os.fdopen(fd, "w", encoding="utf-8") as temp_file:
            json.dump(usuarios, temp_file, indent=4, ensure_ascii=False)
            temp_file.flush()
            os.fsync(temp_file.fileno())
        os.replace(temp_path, archivo)
    except OSError as error:
        try:
            os.remove(temp_path)
        except OSError:
            pass
        raise RuntimeError("No se pudo guardar el archivo de usuarios.") from error
