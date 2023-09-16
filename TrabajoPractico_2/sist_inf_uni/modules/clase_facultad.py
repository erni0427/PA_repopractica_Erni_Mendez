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

    
    def agregar_alumno(self, alumno):
        self.__lista_alumnos.append(alumno)
    
    def asignar_profesor_departamento(self, p_profesor, p_nombre_dpto):
        if isinstance(p_profesor,Profesor):
            for departamento in self.__lista_departamentos:
                if p_nombre_dpto == departamento.nombre:
                    departamento.agregar_profe(p_profesor)


    @property
    def departamentos(self):
        return(self.__lista_departamentos)

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
    
# if __name__ == "__main__":
#     facultad1=Facultad('Facultad de Ingenieria','DepartamentoX')
#     from modules.clase_persona import Alumno
#     alumno1=Alumno('44981249','Sofía','sofiamendez847@gmail.com')
#     alumno2=Alumno('42332860','Esteban','sofiamendez847@gmail.com')
#     facultad1.agregar_alumno(alumno1)
#     facultad1.agregar_alumno(alumno2)
#     facultad1.alumnos
#     print(facultad1)