from modules.clase_persona import Profesor
class Departamento:
    def __init__(self, nombre):
        self.__nombre=nombre
        self.__lista_integrantes=[]
        self.__director= None
    
    @property
    def nombre(self):
        return(self.__nombre)
    
    @property
    def lista_integrantes(self):
        return(self.__lista_integrantes)
    
    @property
    def director(self):
        return(self.__director)

    def agregar_profe(self, p_profesor):
        if isinstance(p_profesor, Profesor):
            self.__lista_integrantes.append(p_profesor)
            p_profesor.agregar_dpto_perteneciente(self)

                 
    def asignar_director(self, p_profesor):
        if isinstance(p_profesor, Profesor):
            if p_profesor in self.__lista_integrantes:
                if not p_profesor.es_jefe:
                    self.__director=p_profesor
                    p_profesor.es_jefe=True
    
    def __str__(self):
        salida=self.__nombre
        return (salida)
    def __repr__(self):
        salida=self.__nombre
        return (salida) #sirve para mostrar objetos dentro de una lista
    
    # def asignar_profesor_departamento(self, p_profesor, p_nombre_dpto):
    #     if isinstance(p_profesor,Profesor):
    #         for departamento in self.__lista_departamentos:
    #             if p_nombre_dpto == departamento.nombre:
    #                 departamento.agregar_profe(p_profesor)
                    #hacer algo parecido pero con curso en vez de departamento