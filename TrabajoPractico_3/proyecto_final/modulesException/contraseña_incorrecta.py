class ContraseñaIncorrecta(Exception):
    def __init__(self, message="Contraseña incorrecta, vuelva a intentarlo"):
        self.message = message
        super().__init__(self.message)