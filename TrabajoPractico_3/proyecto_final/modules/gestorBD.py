# from flask_login import current_user, login_user
# from werkzeug.security import generate_password_hash, check_password_hash
# from modules.databases import ReclamoDB, UsuarioDB  
# from modulesException.userExistence import UsuarioNoExiste, UsuarioYaExiste
# from modulesException.contraseña_incorrecta import ContraseñaIncorrecta
# from modulesException.reclamoExistence import ReclamoNoExiste
# from modules.config import db
# from datetime import datetime
from modules.usuario import Usuario
from modules.reclamo import Reclamo
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

import sqlite3

class GestorBD:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.c = self.conn.cursor()

        # Crear tablas si no existen
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id_usuario INTEGER PRIMARY KEY,
                nombre_usuario TEXT UNIQUE,
                claustro TEXT,
                contrasena TEXT
            )
        ''')
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS reclamos (
                id_reclamo INTEGER PRIMARY KEY,
                id_user_creador INTEGER,
                fecha_hora TEXT,
                depto TEXT,
                descrip_reclamo TEXT,
                estado TEXT,
                FOREIGN KEY (id_user_creador) REFERENCES usuarios(id_usuario)
            )
        ''')
        self.conn.commit()

    def cerrar_conexion(self):
        self.conn.close()

    def guardar_usuario(self, usuario):
        self.c.execute('''
            INSERT INTO usuarios (nombre_usuario, claustro, contrasena)
            VALUES (?, ?, ?)
        ''', (usuario.nombre_usuario, usuario.claustro, usuario.contrasena))
        self.conn.commit()

    def obtener_usuario_por_nombre(self, nombre_usuario):
        self.c.execute('SELECT * FROM usuarios WHERE nombre_usuario = ?', (nombre_usuario,))
        usuario_data = self.c.fetchone()
        if usuario_data:
            usuario = Usuario()
            usuario.id_usuario, usuario.nombre_usuario, usuario.claustro, usuario.contrasena = usuario_data
            return usuario
        else:
            return None

    def guardar_reclamo(self, reclamo):
        self.c.execute('''
            INSERT INTO reclamos (id_user_creador, fecha_hora, depto, descrip_reclamo, estado)
            VALUES (?, ?, ?, ?, ?)
        ''', (reclamo.id_user_creador, reclamo.fecha_hora, reclamo.depto, reclamo.descrip_reclamo, reclamo.estado))
        self.conn.commit()

    def obtener_reclamo_por_id(self, id_reclamo):
        self.c.execute('SELECT * FROM reclamos WHERE id_reclamo = ?', (id_reclamo,))
        reclamo_data = self.c.fetchone()
        if reclamo_data:
            reclamo = Reclamo()
            (
                reclamo.id_reclamo, reclamo.id_user_creador, reclamo.fecha_hora,
                reclamo.depto, reclamo.descrip_reclamo, reclamo.estado
            ) = reclamo_data
            return reclamo
        else:
            return None
