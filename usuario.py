class Usuario:
    def __init__(self, id, nombre, apellidos, email, password):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def convertir_a_diccionario(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "email": self.email,
            "password": self.password
        }