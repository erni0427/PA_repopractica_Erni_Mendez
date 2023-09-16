from modules.clase_persona import Alumno, Profesor
class Curso:

    def __init__(self, nombre, profesor_a_cargo):
        self.__nombre=nombre
        self.__profesor_a_cargo=None
        self.__estudiantes=[]
    
    @property
    def nombre(self):
        return(self.__nombre)

    @property
    def profesor_a_cargo(self):
        return(self.__profesor_a_cargo)
    
    @property
    def estudiantes(self):
        return(self.__estudiantes)

    
    def agregar_alumno(self, p_alumno):
        if isinstance(p_alumno, Alumno):
            self.__estudiantes.append(p_alumno)
            p_alumno.agregar_cursos_inscriptos(self)
        

    
    def agregar_profesor(self, profesor_a_cargo):
        if isinstance(profesor_a_cargo, Profesor):
            self.__profesor_a_cargo.cursos_dictados.append(profesor_a_cargo)
            profesor_a_cargo.agregar_cursos_dictados(self)
 #Para cada curso que dicta un profesor, me pregunto si es el que estoy trabajando actualmente y si es asi lo asigno como profesor a cargo

    def mostrar_estudiantes(self):
        for i in range(len(self.estudiantes)):
            print(self.estudiantes)