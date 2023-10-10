class ReclamoNoExiste(Exception):
    def __init__(self, message="El reclamo no existe"):
        self.message = message
        super().__init__(self.message)