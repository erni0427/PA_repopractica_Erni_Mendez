class Departamento:
    def __init__(self, nombre):
        self.nombre=nombre
        self.lista_integrantes=[]
        self.director= None

    def agregar_profe(self, profesor):
        self.lista_integrantes.append(profesor)
        profesor.dptos.append(self)

    def devolver_integrantes(self):
        return(self.lista_integrantes)
                 
    def elegir_director(self, profesor):
        for profesor in self.lista_integrantes:
            if profesor.es_jefe==True:
                self.director=profesor