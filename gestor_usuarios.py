import json
import os
from usuario import Usuario


class GestorUsuarios:
    def __init__(self, archivo="usuarios.json"):
        self.archivo = archivo
        self.usuarios = []
        self.cargar_usuarios()

    def cargar_usuarios(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as f:
                try:
                    self.usuarios = json.load(f)
                except json.JSONDecodeError:
                    self.usuarios = []
        else:
            self.usuarios = []

    def guardar_usuarios(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(self.usuarios, f, indent=4, ensure_ascii=False)

    def obtener_siguiente_id(self):
        if not self.usuarios:
            return 1
        return max(usuario["id"] for usuario in self.usuarios) + 1

    def email_existe(self, email):
        for usuario in self.usuarios:
            if usuario["email"] == email:
                return True
        return False

    def crear_usuario(self, nombre, apellidos, email, password):
        if not nombre:
            return False, "El nombre es obligatorio."

        if not email:
            return False, "El email es obligatorio."

        if self.email_existe(email):
            return False, "Ya existe un usuario con ese email."

        if len(password) < 8:
            return False, "La contraseña debe tener al menos 8 caracteres."

        nuevo_usuario = Usuario(
            self.obtener_siguiente_id(),
            nombre,
            apellidos,
            email,
            password
        )

        self.usuarios.append(nuevo_usuario.convertir_a_diccionario())
        self.guardar_usuarios()

        return True, "Usuario creado correctamente."

    def listar_usuarios(self):
        return self.usuarios

    def buscar_usuario_por_id(self, id_usuario):
        for usuario in self.usuarios:
            if usuario["id"] == id_usuario:
                return usuario
        return None

    def modificar_usuario(self, id_usuario, nombre, apellidos, email):
        usuario = self.buscar_usuario_por_id(id_usuario)

        if usuario is None:
            return False, "No existe un usuario con ese ID."

        if not nombre:
            return False, "El nombre es obligatorio."

        if not email:
            return False, "El email es obligatorio."

        for otro_usuario in self.usuarios:
            if otro_usuario["email"] == email and otro_usuario["id"] != id_usuario:
                return False, "Ya existe otro usuario con ese email."

        usuario["nombre"] = nombre
        usuario["apellidos"] = apellidos
        usuario["email"] = email

        self.guardar_usuarios()

        return True, "Usuario modificado correctamente."

    def eliminar_usuario(self, id_usuario):
        usuario = self.buscar_usuario_por_id(id_usuario)

        if usuario is None:
            return False, "No existe un usuario con ese ID."

        self.usuarios.remove(usuario)
        self.guardar_usuarios()

        return True, "Usuario eliminado correctamente."