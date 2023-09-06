from modules.clase_departamento import Departamento

class Facultad:
    def __init__ (self,departamento_inicial):
        departamento1=Departamento(departamento_inicial)
        self.lista_departamentos=[]
        self.lista_departamentos.append(departamento1)
        self.lista_alumnos = []
    def agregar_alumno(self, alumno):
        self.lista_alumnos.append(alumno)
    def mostrar_alumnos(self):
        for alumno in self.lista_alumnos:
            print(alumno.nombre)
    def mostrar_departamentos(self):
        for dpto in self.lista_departamentos:
            print(dpto.nombre)
    def crear_departamentos(self, nombre):
        departamento=Departamento(nombre)
        self.lista_departamentos.append(departamento)
    def asignar_docente(self, profesor, departamento):
        for i in self.lista_departamentos:
            if i.nombre==departamento:
                i.agregar_profe(profesor)
        return()
    def asignar_jefe(self, departamento, profesor):
        for i in self.lista_departamentos:
            if i.nombre==departamento:
                i.elegir_director(profesor)
        return()
    def devolver_equipo(self, departamento):
        for i in self.lista_departamentos:
            if i.nombre==departamento:
                lista=i.devolver_integrantes()
                return(lista)