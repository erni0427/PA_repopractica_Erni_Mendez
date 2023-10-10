
class UsuarioYaExiste(Exception):    
    def __init__(self, msg):
        self.msg = msg

class UsuarioNoExiste(Exception):    
    def __init__(self, message="El usuario no existe"):
            self.message = message
            super().__init__(self.message)
