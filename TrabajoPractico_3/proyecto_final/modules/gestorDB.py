from flask_login import current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from modules.databases import ReclamoDB, UsuarioDB  
from modulesException.userExistence import UsuarioNoExiste, UsuarioYaExiste
from modulesException.contraseña_incorrecta import ContraseñaIncorrecta
from modulesException.reclamoExistence import ReclamoNoExiste
from modules.config import db
from datetime import datetime

class GestorDB():
    #sirve como una especie de controlador para interactuar con la base de datos y realizar operaciones 
    # relacionadas con usuarios y reclamos.

    def __init__(self):
        pass

    def crear_usuarioDB(self, register_form):
        #El método se encarga de verificar si el usuario ya existe en la base de datos y, si no existe, 
        # crea un nuevo usuario en la base de datos.

        if UsuarioDB.query.filter_by(email=register_form.email.data).first():
            raise UsuarioYaExiste('El usuario ya existe en la base de datos')

        encripted_pass = generate_password_hash(
            password=register_form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )

        new_user = UsuarioDB(
            email=register_form.email.data,
            password=encripted_pass,
            user_name=register_form.username.data,
            lastname=register_form.apellido.data,
            name=register_form.nombre.data,
            claustro=register_form.claustro.data
        )
        db.session.add(new_user)
        db.session.commit()

    def crear_reclamoDB(self, reclamo_form, usuario_id):
        # Obtén los datos del formulario de reclamo
        titulo = reclamo_form.titulo.data
        descripcion = reclamo_form.descripcion.data
        fecha_creacion = datetime.now()  # Asigna la fecha actual
        # usuario_id se pasa como argumento al método para vincular el reclamo al usuario que lo crea

        # Crea un nuevo objeto ReclamoDB con los datos del formulario
        nuevo_reclamo = ReclamoDB(
            titulo=titulo,
            descripcion=descripcion,
            fecha_creacion=fecha_creacion,
            usuario_id=usuario_id
        )

        # Agrega el nuevo reclamo a la sesión de la base de datos y guarda los cambios
        db.session.add(nuevo_reclamo)
        db.session.commit()
    def modificar_reclamo(self, reclamo_id, nuevo_titulo, nueva_descripcion):
        # Busca el reclamo por su ID
        reclamo = ReclamoDB.query.get(reclamo_id)

        if reclamo:
            # Actualiza los campos del reclamo con los nuevos valores
            reclamo.titulo = nuevo_titulo
            reclamo.descripcion = nueva_descripcion

            # Guarda los cambios en la base de datos
            db.session.commit()
        else:
            raise ReclamoNoExiste("El reclamo no existe")

    def acceso_usuario(self, login_form):
        #Este método toma como argumento un formulario de inicio de sesión ( login_form) que contiene el correo electrónico y 
        # la contraseña del usuario que intenta iniciar sesión. El método verifica si el usuario existe en la base de datos y si la 
        # contraseña proporcionada coincide con la contraseña almacenada en la base de datos. Si todo es válido, inicia sesión al 
        # usuario utilizando Flask-Login.

        email = login_form.email.data
        password = login_form.password.data

        user = UsuarioDB.query.filter_by(email=email).first()
        if not user:
            raise UsuarioNoExiste("El email no existe, vuelva a intentarlo")
        elif not check_password_hash(user.password, password):
            raise ContraseñaIncorrecta("Contraseña incorrecta, vuelva a intentarlo")
        else:
            login_user(user)

    def mostrar_reclamos(self):
        #Este método consulta todos los reclamos en la base de datos y los devuelve en forma de una lista de reclamos. Luego, estos 
        # reclamos pueden ser utilizados para mostrarlos en la interfaz de usuario o para realizar otras operaciones.
        reclamos = ReclamoDB.query.all()
        return reclamos