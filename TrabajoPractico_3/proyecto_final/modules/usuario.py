class Usuario():
    """Modela un objeto que ingresa a la aplicación"""
    def __init__(self):
        self.__id_usuario = None
        self.__mis_reclamos = []
        self.__nombre_usuario = None

    @property
    def id_usuario(self):
        return self.__id_usuario
    
    @id_usuario.setter
    def id_usuario(self, id_user:int):
        self.__id_usuario = id_user
    
        
    @property
    def mis_reclamos(self):
        return self.__mis_reclamos
    
    @mis_reclamos.setter
    def mis_reclamos(self, mis_reclamos:list):
        self.__mis_reclamos = mis_reclamos
    
    
    @property
    def nombre_usuario(self):
        return self.__nombre_usuario
    
    
    def adherir_id_reclamo(self, id_reclamo:int):
        if id_reclamo not in self.mis_reclamos:
            self.mis_reclamos.append(id_reclamo)