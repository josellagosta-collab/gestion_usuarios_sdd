from gestor_usuarios import GestorUsuarios


def test_crear_usuario_correcto():
    gestor = GestorUsuarios("test_usuarios.json")
    gestor.usuarios = []
    gestor.guardar_usuarios()

    correcto, mensaje = gestor.crear_usuario(
        "Jose", "Aguilera", "jose@test.com", "12345678"
    )

    assert correcto is True
    assert len(gestor.usuarios) == 1
    assert gestor.usuarios[0]["password"] != "12345678"
    assert gestor.usuarios[0].get("salt")


def test_email_duplicado():
    gestor = GestorUsuarios("test_usuarios.json")
    gestor.usuarios = []
    gestor.guardar_usuarios()

    gestor.crear_usuario("Jose", "Aguilera", "jose@test.com", "12345678")

    correcto, mensaje = gestor.crear_usuario(
        "Ana", "Lopez", "jose@test.com", "87654321"
    )

    assert correcto is False
    assert mensaje == "Ya existe un usuario con ese email."


def test_email_formato_invalido():
    gestor = GestorUsuarios("test_usuarios.json")
    gestor.usuarios = []
    gestor.guardar_usuarios()

    correcto, mensaje = gestor.crear_usuario(
        "Luis", "Garcia", "luis-at-test.com", "12345678"
    )

    assert correcto is False
    assert mensaje == "El email no tiene un formato válido."


def test_password_corta():
    gestor = GestorUsuarios("test_usuarios.json")
    gestor.usuarios = []
    gestor.guardar_usuarios()

    correcto, mensaje = gestor.crear_usuario("Luis", "Garcia", "luis@test.com", "123")

    assert correcto is False
    assert mensaje == "La contraseña debe tener al menos 8 caracteres."


def test_eliminar_usuario():
    gestor = GestorUsuarios("test_usuarios.json")
    gestor.usuarios = []
    gestor.guardar_usuarios()

    gestor.crear_usuario("Marta", "Perez", "marta@test.com", "12345678")

    correcto, mensaje = gestor.eliminar_usuario(1)

    assert correcto is True
    assert len(gestor.usuarios) == 0


def test_eliminar_usuario_inexistente():
    gestor = GestorUsuarios("test_usuarios.json")
    gestor.usuarios = []
    gestor.guardar_usuarios()

    correcto, mensaje = gestor.eliminar_usuario(999)

    assert correcto is False
    assert mensaje == "No existe un usuario con ese ID."


def test_modificar_usuario_conflicto_email():
    gestor = GestorUsuarios("test_usuarios.json")
    gestor.usuarios = []
    gestor.guardar_usuarios()

    gestor.crear_usuario("Jose", "Aguilera", "jose@test.com", "12345678")
    gestor.crear_usuario("Ana", "Lopez", "ana@test.com", "87654321")

    correcto, mensaje = gestor.modificar_usuario(2, "Ana", "Lopez", "jose@test.com")

    assert correcto is False
    assert mensaje == "Ya existe otro usuario con ese email."
