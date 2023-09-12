class Curso:

    def __init__(self, nombre, profesor_a_cargo):
        self.nombre=nombre
        self.profesor_a_cargo=None
        self.estudiantes=[]
    
    def agregar_alumno(self, alumno):
        self.estudiantes.append(alumno)
        alumno.cursos_inscripto_alumno.append(self)
    
    def agregar_profesor(self, profesor_a_cargo):
        profesor_a_cargo.cursos_dictados.append(self)
 #Para cada curso que dicta un profesor, me pregunto si es el que estoy trabajando actualmente y si es asi lo asigno como profesor a cargo

    def mostrar_estudiantes(self):
        for i in range(len(self.estudiantes)):
            print(self.estudiantes)