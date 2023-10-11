import datetime

class Reclamo():
    def __init__(self):
        self.__estado = 'Pendiente'
        self.__id_reclamo = None
        self.__id_user_creador = None
        self.__fecha_hora = str(datetime.datetime.now())
        self.__depto = "Secretaría Técnica"
        self.__descrip_reclamo = None
        self.__id_adherentes = []
        
    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, estado:str):     
        self.__estado = estado

    @property
    def id_reclamo(self):
        return self.__id_reclamo
    
    @id_reclamo.setter
    def id_reclamo(self, id_reclamo):
        self.__id_reclamo = id_reclamo

    @property
    def id_user_creador(self):
        return self.__id_user_creador
    
    @property   
    def fecha_hora(self):
        return self.__fecha_hora
        
    @property
    def depto(self):
        return self.__depto
    
    @depto.setter
    def depto(self, depto):
        self.__depto = depto
            
    @property
    def descrip_reclamo(self):
        return self.__descrip_reclamo
    
    @descrip_reclamo.setter
    def descrip_reclamo(self, descrip_reclamo):
        self.__descrip_reclamo = descrip_reclamo
    
    @property
    def id_adherentes(self):
        return self.__id_adherentes
    
    @id_adherentes.setter
    def id_adherentes(self, id_adherentes:list):
        self.__id_adherentes = id_adherentes
    
