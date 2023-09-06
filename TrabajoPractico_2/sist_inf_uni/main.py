from modules.clase_curso import Curso
from modules.clase_facultad import Facultad
from modules.clase_persona import Alumno, Profesor

facultad=Facultad('Departamento de Informática')
curso=Curso('Programación Avanzada')
alumno1=Alumno('44981249','Sofía','sofiamendez847@gmail.com')
profesor1=Profesor('20338023', 'Isidora Zibecchi', 'abo_zibecchi@hotmail.com', True, None)

facultad.agregar_alumno(alumno1)

facultad.mostrar_alumnos()

facultad.crear_departamentos('Departamento de Programación')

facultad.mostrar_departamentos()

alumno1.mostrar_datos()

curso.agregar_alumno(alumno1)

curso.mostrar_estudiantes()

curso.agregar_profesor(profesor1)

curso.mostrar_catedra()

facultad.asignar_docente(profesor1,"Departamento de Informática")

facultad.asignar_jefe("Departamento de Informática",profesor1)

lista_integrantes_departamento_informatica=facultad.devolver_equipo("Departamento de Informática")

print(lista_integrantes_departamento_informatica)