from gestor_usuarios import GestorUsuarios


def test_crear_usuario_correcto():
    gestor = GestorUsuarios("test_usuarios.json")
    gestor.usuarios = []
    gestor.guardar_usuarios()

    correcto, mensaje = gestor.crear_usuario(
        "Jose",
        "Aguilera",
        "jose@test.com",
        "12345678"
    )

    assert correcto is True
    assert len(gestor.usuarios) == 1


def test_email_duplicado():
    gestor = GestorUsuarios("test_usuarios.json")
    gestor.usuarios = []
    gestor.guardar_usuarios()

    gestor.crear_usuario(
        "Jose",
        "Aguilera",
        "jose@test.com",
        "12345678"
    )

    correcto, mensaje = gestor.crear_usuario(
        "Ana",
        "Lopez",
        "jose@test.com",
        "87654321"
    )

    assert correcto is False
    assert mensaje == "Ya existe un usuario con ese email."


def test_password_corta():
    gestor = GestorUsuarios("test_usuarios.json")
    gestor.usuarios = []
    gestor.guardar_usuarios()

    correcto, mensaje = gestor.crear_usuario(
        "Luis",
        "Garcia",
        "luis@test.com",
        "123"
    )

    assert correcto is False
    assert mensaje == "La contraseña debe tener al menos 8 caracteres."


def test_eliminar_usuario():
    gestor = GestorUsuarios("test_usuarios.json")
    gestor.usuarios = []
    gestor.guardar_usuarios()

    gestor.crear_usuario(
        "Marta",
        "Perez",
        "marta@test.com",
        "12345678"
    )

    correcto, mensaje = gestor.eliminar_usuario(1)

    assert correcto is True
    assert len(gestor.usuarios) == 0