# from flask_login import current_user, login_user
# from werkzeug.security import generate_password_hash, check_password_hash
# from modules.databases import ReclamoDB, UsuarioDB  
# from modulesException.userExistence import UsuarioNoExiste, UsuarioYaExiste
# from modulesException.contraseña_incorrecta import ContraseñaIncorrecta
# from modulesException.reclamoExistence import ReclamoNoExiste
# from modules.config import db
# from datetime import datetime

# class GestorDB():
#     #sirve como una especie de controlador para interactuar con la base de datos y realizar operaciones 
#     # relacionadas con usuarios y reclamos.

#     def __init__(self):
#         pass
    
    
#     def guardar_usuarioDB(self,usuario):
#         #El método se encarga de verificar si el usuario ya existe en la base de datos y, si no existe, 
#         # crea un nuevo usuario en la base de datos.

#         new_user = UsuarioDB(
#             email=dic['email'],
#             password=dic['pass'],
#             user_name=dic['username'],
#             lastname=dic['apellido'],
#             name=dic['nombre'],
#             claustro=dic['claustro']
#         )
#         db.session.add(new_user)
#         db.session.commit()

#     def guardar_reclamoDB(self, reclamo):
#         # Crea un nuevo objeto ReclamoDB con los datos del formulario
#         nuevo_reclamo = ReclamoDB(
#             titulo=dic['titulo'],
#             descripcion=dic['descripcion'],
#             fecha_creacion=dic['fecha_creacion'],
#             usuario_id=dic['usuario_id'],
#         )

#         # Agrega el nuevo reclamo a la sesión de la base de datos y guarda los cambios
#         db.session.add(nuevo_reclamo)
#         db.session.commit()
    
    
# # if__name__=="__main__":


