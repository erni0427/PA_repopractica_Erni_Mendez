class Curso:

    def __init__(self, nombre):
        self.nombre=nombre
        self.catedra=[]
        self.estudiantes=[]
    
    def agregar_alumno(self, alumno):
        self.estudiantes.append(alumno)
        alumno.cursos_inscriptos_alumnos.append(self)
    
    def agregar_profesor(self, profesor):
        self.catedra.append(profesor)
        profesor.cursos_dictados.append(self)


    def mostrar_catedra(self):
        for i in range(len(self.catedra)):
            print(self.catedra)

    def mostrar_estudiantes(self):
        for i in range(len(self.estudiantes)):
            print(self.estudiantes)