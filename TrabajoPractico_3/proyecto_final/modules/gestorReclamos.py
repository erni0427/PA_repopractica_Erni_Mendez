from modules.reclamo import Reclamo
# class GestorReclamos():

#     def __init__(self):
#         self.__reclamo=

#     # def construir_reclamo(self,dic):
#     #     titulo=dic['titulo']
#     #     descripcion=dic['descripcion']
#     #     fecha=dic['fecha_creacion']
#     #     reclamo=Reclamo
#     #     reclamo.id_reclamo=
#     #     #completar todos los atributos
#     #     reclamo.fecha_hora=fecha
#     #     self.__estado = 'Pendiente'
#     #     self.__id_reclamo = None
#     #     self.__id_user_creador = None
#     #     self.__fecha_hora = str(datetime.datetime.now())
#     #     self.__depto = "Secretaría Técnica"
#     #     self.__descrip_reclamo = None
#     #     self.__id_adherentes = []
#     #     return reclamo

#     def modificar_reclamo(self, dic, nuevo_titulo, nueva_descripcion):
#             # Busca el reclamo por su ID
#             reclamo = ReclamoDB.query.get(dic['reclamo_id'])

#             if reclamo:
#                 # Actualiza los campos del reclamo con los nuevos valores
#                 dic['titulo'] = nuevo_titulo
#                 dic['descripcion'] = nueva_descripcion

#                 # Guarda los cambios en la base de datos
#                 db.session.commit()
#             else:
#                 raise ReclamoNoExiste("El reclamo no existe")

#     def acceso_usuario(self, login_form):
#         #Este método toma como argumento un formulario de inicio de sesión ( login_form) que contiene el correo electrónico y 
#         # la contraseña del usuario que intenta iniciar sesión. El método verifica si el usuario existe en la base de datos y si la 
#         # contraseña proporcionada coincide con la contraseña almacenada en la base de datos. Si todo es válido, inicia sesión al 
#         # usuario utilizando Flask-Login.

#         email = login_form.email.data
#         password = login_form.password.data

#         user = UsuarioDB.query.filter_by(email=email).first()
#         if not user:
#             raise UsuarioNoExiste("El email no existe, vuelva a intentarlo")
#         elif not check_password_hash(user.password, password):
#             raise ContraseñaIncorrecta("Contraseña incorrecta, vuelva a intentarlo")
#         else:
#             login_user(user)

#     def mostrar_reclamos(self):
#         #Este método consulta todos los reclamos en la base de datos y los devuelve en forma de una lista de reclamos. Luego, estos 
#         # reclamos pueden ser utilizados para mostrarlos en la interfaz de usuario o para realizar otras operaciones.
#         reclamos = ReclamoDB.query.all()
#         return reclamos
class GestorDeReclamos:
    def __init__(self):
        self.usuarios = []  # Lista para almacenar usuarios
        self.reclamos = []  # Lista para almacenar reclamos

    def registrar_usuario(self, usuario):
        # Comprobar si el nombre de usuario o correo ya existen
        if any(u.nombre_usuario == usuario.nombre_usuario or u.id_usuario == usuario.id_usuario for u in self.usuarios):
            print("Nombre de usuario o correo electrónico ya existen. Por favor, elija otro.")
            return False

        self.usuarios.append(usuario)
        print("Usuario registrado exitosamente.")
        return True

    def crear_reclamo(self, usuario, descripcion):
        reclamo = Reclamo()
        reclamo.id_reclamo = len(self.reclamos) + 1
        reclamo.id_user_creador = usuario.id_usuario
        reclamo.descrip_reclamo = descripcion
        self.reclamos.append(reclamo)
        return reclamo

    def listar_reclamos(self, departamento=None):
        if departamento:
            reclamos = [r for r in self.reclamos if r.depto == departamento]
        else:
            reclamos = self.reclamos
        return reclamos

    def adherir_a_reclamo(self, usuario, reclamo):
        if reclamo.estado == "Pendiente":
            if usuario.id_usuario not in reclamo.id_adherentes:
                reclamo.id_adherentes.append(usuario.id_usuario)
                print("Adherido al reclamo con éxito.")
            else:
                print("Ya está adherido a este reclamo.")
        else:
            print("No se puede adherir a un reclamo que no está pendiente.")

    def actualizar_estado_reclamo(self, reclamo, nuevo_estado):
        reclamo.estado = nuevo_estado
        print(f"Estado del reclamo actualizado a '{nuevo_estado}'.")

# Ejemplo de uso del GestorDeReclamos
