from usuario import Usuario


def test_crear_usuario_hash_password():
    usuario = Usuario.crear_con_password(
        1,
        "Carlos",
        "Santana",
        "carlos@test.com",
        "contrasena123",
    )

    assert usuario.password != "contrasena123"
    assert usuario.salt
    assert usuario.verificar_password("contrasena123") is True
    assert usuario.verificar_password("otra") is False
