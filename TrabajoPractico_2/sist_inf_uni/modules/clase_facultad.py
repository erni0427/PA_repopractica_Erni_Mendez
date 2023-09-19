from modules.clase_departamento import Departamento
from modules.clase_persona import Alumno, Profesor

class Facultad:
    def __init__ (self,nombre,departamento_inicial):
        self.__lista_departamentos=[Departamento(departamento_inicial)]
        self.__lista_alumnos = []
        self.__nombre = nombre
    #.set para agregar y get para mostrar q se usa con property

    @property
    def lista_departamentos(self):
        return(self.__lista_departamentos)

    @property
    def lista_alumnos(self):
        return(self.__lista_alumnos)
    
    @property
    def nombre(self):
        return(self.__nombre)

    
    def agregar_alumno(self, p_alumno):
        self.__lista_alumnos.append(p_alumno)
    
    def asignar_profesor_departamento(self, p_profesor, p_nombre_dpto):
        if isinstance(p_profesor,Profesor):
            for departamento in self.__lista_departamentos:
                if p_nombre_dpto == departamento.nombre:
                    departamento.agregar_profe(p_profesor)

    def crear_departamentos(self, nombre):
        departamento=Departamento(nombre)
        self.__lista_departamentos.append(departamento)

    def devolver_equipo(self):
        lista=[]
        for i in self.__lista_departamentos:
            lista.append(i.lista_integrantes)
        return(lista)
            #Recorre todos los departamentos y por cada departamento muestra todos los profesores integrantes
    def __str__(self):
        salida=self.__nombre
        return (salida)
    
    def __repr__(self):
        salida=self.__nombre
        return (salida) #sirve para mostrar objetos dentro de una lista
    
