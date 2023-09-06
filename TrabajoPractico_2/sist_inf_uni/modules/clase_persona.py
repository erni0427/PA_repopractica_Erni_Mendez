class Persona:
    def __init__(self, DNI, nombre, correo):
        self.DNI= DNI
        self.nombre= nombre
        self.correo= correo

    def mostrar_datos(self):
        print(self.nombre + " - " + self.DNI + " - " + self.correo)

    def mostrar_cursos(self):
        for i in self.cursos:
            print(i.nombre)
    

class Alumno(Persona):
    def __init__(self, DNI, nombre, correo):
        super().__init__(DNI, nombre, correo)
        self.cursos_inscriptos_alumnos=[]

class Profesor(Persona):
    
    def __init__(self, DNI, nombre, correo, es_jefe, dpto):
        super().__init__(DNI, nombre, correo)
        self.es_jefe = es_jefe
        self.dptos=[dpto]
        self.cursos_dictados=[]
    

#cursos inscriptos pasan a ser atributos de las clases hijas ya que son diferentes las acciones que hacen con esos cursos, 
# un alumno cursa, un profesor enseña