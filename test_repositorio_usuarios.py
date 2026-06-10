from pathlib import Path

from repositorio_usuarios import cargar_usuarios, guardar_usuarios


def test_guardar_y_cargar_usuarios(tmp_path: Path):
    archivo = tmp_path / "usuarios.json"
    usuarios = [
        {
            "id": 1,
            "nombre": "Prueba",
            "apellidos": "Test",
            "email": "prueba@test.com",
            "password": "hash",
            "salt": "salts",
        }
    ]

    guardar_usuarios(str(archivo), usuarios)
    cargados = cargar_usuarios(str(archivo))

    assert cargados == usuarios


def test_cargar_json_corrupto_devuelve_lista_vacia(tmp_path: Path):
    archivo = tmp_path / "usuarios.json"
    archivo.write_text("{ malformed json", encoding="utf-8")

    usuarios = cargar_usuarios(str(archivo))

    assert usuarios == []
