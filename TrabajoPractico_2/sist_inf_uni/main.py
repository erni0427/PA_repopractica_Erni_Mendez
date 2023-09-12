from modules.clase_curso import Curso
from modules.clase_facultad import Facultad
from modules.clase_persona import Alumno, Profesor
from modules.clase_departamento import Departamento

facultad=Facultad("Facultad de Ingenieria","Departamento X")
profesor1=Profesor('20338023', 'Isidora Zibecchi', 'abo_zibecchi@hotmail.com', True, None)
curso=Curso('Programación Avanzada', profesor1)
alumno1=Alumno('44981249','Sofía','sofiamendez847@gmail.com')
 
#El None hace referencia a que no tiene un departamento asiganado aun

facultad.agregar_alumno(alumno1)

facultad.mostrar_alumnos()

departamento_X=facultad.lista_departamentos[0]
#departamento_X.agregar_profe(profesor1)
print(facultad)
print(departamento_X)

"""facultad.crear_departamentos('Departamento de Programación')

departamento2.agregar_profe(profesor1)

facultad.mostrar_departamentos()

facultad.devolver_equipo()

alumno1.mostrar_datos()

curso.agregar_alumno(alumno1)

curso.mostrar_estudiantes()

curso.agregar_profesor(profesor1)

curso.mostrar_catedra()

facultad.asignar_docente(profesor1,"Departamento de Informática")

facultad.asignar_jefe("Departamento de Informática",profesor1)

lista_integrantes_departamento_informatica=facultad.devolver_equipo("Departamento de Informática")

print(lista_integrantes_departamento_informatica)"""