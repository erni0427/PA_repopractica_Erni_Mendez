from modules.clase_persona import Profesor
from modules.clase_curso import Curso
class Departamento: #diseñada para gestionar profesores, cursos y la asignación de un director al departamento.
    #se inicializan clases del dpto
    def __init__(self, nombre):
        self.__nombre=nombre
        self.__lista_integrantes=[] #lista de profes
        self.__director= None
        self.__lista_cursos=[]
    
    @property
    def nombre(self):
        return(self.__nombre)
    
    @property
    def lista_integrantes(self):
        return(self.__lista_integrantes)
    
    @property
    def director(self):
        return(self.__director)
    
    @property
    def lista_cursos(self):
        return(self.__lista_cursos)

    def agregar_profe(self, p_profesor):
        if isinstance(p_profesor, Profesor): #recibe obj y clase, p ver si dicho objeto pertenece a la clase.
            self.__lista_integrantes.append(p_profesor) #agrego prof a lista de prof
            p_profesor.agregar_dpto_perteneciente(self) #agrego dpto a los pertenecientes del prof

                 
    def asignar_director(self, p_profesor):
        if isinstance(p_profesor, Profesor):
            if p_profesor in self.__lista_integrantes: #verif si profesor esta ya en el dpto
                if not p_profesor.es_jefe: #antes de asignarlo como director, verifica q ya no lo sea
                    self.__director=p_profesor #si es false lo agrega
                    p_profesor.es_jefe=True #indica q ahora este profe es jefe

    
    
    def asignar_profesor_curso(self, p_profesor, p_curso):
            if isinstance(p_profesor,Profesor):
                for curso in self.__lista_cursos: #recorre la lista de cursos, busca el curso especificado
                    if p_curso == curso.nombre: #verif si el nombre del cursoacutal coincide con el curso esppec en p.curso
                        curso.agregar_profesor(p_profesor) #si encuentra asocia el curso con el profe
                        
    def agregar_curso(self, p_curso):
        if isinstance(p_curso,Curso):
            if p_curso not in self.__lista_cursos:
                self.__lista_cursos.append(p_curso)
                p_curso.agregar_dpto_perteneciente(self) #agreg curso a pertenecientes del prof
    
    def __str__(self):
        salida=self.__nombre
        return (salida)
    def __repr__(self):
        salida=self.__nombre
        return (salida) #sirve para mostrar objetos dentro de una lista