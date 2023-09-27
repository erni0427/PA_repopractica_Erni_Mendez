from modules.clase_departamento import Departamento
from modules.clase_persona import Alumno, Profesor
from modules.clase_curso import Curso

class Facultad: #se construye clase
    def __init__ (self,nombre,departamento_inicial): #arg
        self.__lista_departamentos=[Departamento(departamento_inicial)] #1er dpto q se crea y se agrega a la lista
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
    
    def devolver_director_dpto(self,p_nombre_dpto): #self se refiere  faucltad
        for departamento in self.__lista_departamentos: #recorre listadptos
            if p_nombre_dpto == departamento.nombre: #verif si el nombredpto es igual al q se paso como argum
                return(departamento.director) #si es asi se devuelve el nombre del director del dpto
            
    def devolver_lista_cursos_departamento(self, p_nombre_dpto):
        for departamento in self.__lista_departamentos:
            if p_nombre_dpto == departamento.nombre:
                return(departamento.lista_cursos) #cursos q pertenecen al dpto
    
    def agregar_alumno(self, p_alumno):
        self.__lista_alumnos.append(p_alumno)
    
    def agregar_curso_departamento(self,p_curso,p_nombre_dpto):
        if isinstance(p_curso, Curso):
            for departamento in self.__lista_departamentos:
                if p_nombre_dpto == departamento.nombre:
                    departamento.agregar_curso(p_curso) #agregar curso viene depto
    
    def asignar_director_departamento(self, p_profesor, p_nombre_dpto):
        if isinstance(p_profesor, Profesor):
            for departamento in self.__lista_departamentos:
                if p_nombre_dpto == departamento.nombre:
                    departamento.asignar_director(p_profesor)
    
    def asignar_profesor_departamento(self, p_profesor, p_nombre_dpto):
        if isinstance(p_profesor,Profesor):
            for departamento in self.__lista_departamentos:
                if p_nombre_dpto == departamento.nombre:
                    departamento.agregar_profe(p_profesor)

    def crear_departamentos(self, nombre): #nombre del dpto a crear
        departamento=Departamento(nombre) #se crea instancia dpto
        self.__lista_departamentos.append(departamento) #se agrega a la list de dptos

    def devolver_equipo(self): #se obtiene lista de lista de prof de cda dpto
        lista=[] 
        for i in self.__lista_departamentos: #en cada i se obtiene lista de prof de cda dpto
            lista.append(i.lista_integrantes)
        return(lista)
            #Recorre todos los departamentos y por cada departamento muestra todos los profesores integrantes
    def __str__(self):
        salida=self.__nombre
        return (salida)
    
    def __repr__(self):
        salida=self.__nombre
        return (salida) #sirve para mostrar objetos dentro de una lista
    
