import json
from pathlib import Path

from main import main


def test_main_crear_usuario_cli(tmp_path: Path):
    archivo = tmp_path / "usuarios.json"
    exit_code = main([
        "--archivo",
        str(archivo),
        "crear",
        "--nombre",
        "CLI",
        "--apellidos",
        "Usuario",
        "--email",
        "cli@test.com",
        "--password",
        "12345678",
    ])

    assert exit_code == 0
    assert archivo.exists()

    with archivo.open("r", encoding="utf-8") as f:
        usuarios = json.load(f)

    assert len(usuarios) == 1
    assert usuarios[0]["email"] == "cli@test.com"
    assert usuarios[0]["password"] != "12345678"
