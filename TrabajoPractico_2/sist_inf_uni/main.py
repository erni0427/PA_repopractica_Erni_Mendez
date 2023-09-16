from modules.clase_curso import Curso
from modules.clase_facultad import Facultad
from modules.clase_persona import Alumno, Profesor


facultad=Facultad("Facultad de Ingenieria","Departamento X")
profesor1=Profesor('20338023', 'Isidora Zibecchi', 'abo_zibecchi@hotmail.com')
profesor2=Profesor('21129054', 'Mario Erni', 'mario.erni2gmail.com')
curso=Curso('Programación Avanzada', profesor1)
alumno1=Alumno('44981249','Sofía Mendez','sofiamendez847@gmail.com')
 


facultad.agregar_alumno(alumno1)

print(facultad.lista_alumnos)


facultad.asignar_profesor_departamento(profesor1,"Departamento X")

facultad.crear_departamentos('Departamento de Programación')
facultad.asignar_profesor_departamento(profesor2,"Departamento de Programación")
print(facultad.departamentos)


print(facultad.devolver_equipo())

# alumno1.mostrar_datos()

# curso.agregar_alumno(alumno1)

# curso.mostrar_estudiantes()

# curso.agregar_profesor(profesor1)

# curso.mostrar_catedra()

# facultad.asignar_docente(profesor1,"Departamento de Informática")

# facultad.asignar_jefe("Departamento de Informática",profesor1)

# lista_integrantes_departamento_informatica=facultad.devolver_equipo("Departamento de Informática")

# print(lista_integrantes_departamento_informatica)