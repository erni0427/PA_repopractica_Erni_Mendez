from modules.config import db
from modules.usuario import Usuario
from modules.reclamo import Reclamo
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Text, Table
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy.orm import relationship
from modulesException.userExistence import UsuarioNoExiste
from modulesException.reclamoExistence import ReclamoNoExiste

#crear los reclamos y usuarios en la base de datos
#https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html

reclamos_usuarios = db.Table('reclamos_usuarios',
                          Column('claims_id', Integer, ForeignKey('claims.id'), primary_key=True),
                          Column('users_id', Integer, ForeignKey('users.id'), primary_key=True))

class ReclamoDB(db.Model):
    __tablename__ = 'claims'
    #SQLAlchemy generará automáticamente un id único y lo asignará al objeto nuevo_reclamo 
    #cuando se realice la operación db.session.commit()
    id = Column(Integer(), primary_key=True)
    id_usuario_creador = Column(Integer(), ForeignKey('users.id'), nullable=False) #id del usuario que lo creo
    fecha_hora = Column(DateTime(), default=datetime.now())
    depto = Column(String(50), nullable=False) #cambia el dpto derivar_reclamo
    estado = Column(String(50), nullable=False)
    text = Column(Text(), nullable=False)
    usuarios_adheridos = relationship('UsuarioDB', secondary=reclamos_usuarios, backref='reclamos', lazy='dynamic', overlaps="reclamos_adheridos")

    def __repr__(self):
        return f'{self.id}'

class UsuarioDB(UserMixin, db.Model):
    __tablename__ = 'users'
    #SQLAlchemy generará automáticamente un id único y lo asignará al objeto new_user 
    #cuando se realice la operación db.session.commit()
    id = Column(Integer(), primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100), nullable=False)
    name = Column(String(1000), nullable=False)
    lastname = Column(String(1000), nullable=False)
    user_name = Column(String(100), nullable=False, unique=True)
    claustro = Column(String(100), nullable=False)
    reclamos_creados = relationship('ReclamoDB', backref = 'users', lazy=True)
    reclamos_adheridos = relationship('ReclamoDB', secondary=reclamos_usuarios, backref='usuarios', lazy='dynamic', overlaps="reclamos_adheridos")

    def __repr__(self):
        return f'{self.user_name}'
    


#crear usuarios en el sistema 
def crear_usuario(p_usuarioDB:UsuarioDB) -> Usuario:
    #Esta función toma un objeto de la clase UsuarioDB como entrada y devuelve un objeto de la clase Usuario.
    user = Usuario()
    #Guardamos el id generado en el objeto de la clase Usuario
    user.id_usuario = p_usuarioDB.id_usuario
    return user

#crear reclamo en el sistema
def crear_reclamo(p_reclamoDB:ReclamoDB) -> Reclamo:
    #Esta función toma un objeto de la clase ReclamoDBcomo entrada y devuelve un objeto de la clase Reclamo.
    claim = Reclamo()
    #Guardamos el id generado en el objeto de la clase Reclamo
    claim.id_reclamo = p_reclamoDB.id_reclamo
    return claim

#muestra los reclamos que creo el usuario (usando claves foraneas)
def mostrar_reclamos_creados(p_id_usuario:int) -> list:

    user = UsuarioDB.query.get(p_id_usuario)
    reclamos = user.reclamos_creados
    list_reclamos = [ r.id for r in reclamos ]
    return list_reclamos

#muestra los reclamos a los que esta adherido el usuario (aca se usa la tabla reclamos_usuarios )
def mostrar_reclamos_adheridos(p_id_usuario:int) -> list:
    try:
        usuario = db.session.query(UsuarioDB).filter_by(id=p_id_usuario).first()
        # Verificar si se encontró el usuario
        if usuario:
            # Acceder a los reclamos adheridos por el usuario
            reclamos_adheridos = usuario.reclamos_adheridos.all()
            # Iterar sobre los reclamos adheridos y obtener sus detalles
            lista=[]
            for reclamo in reclamos_adheridos:
                lista.append(reclamo.id)
            lista.sort()
            return print(lista)
        else:
            raise UsuarioNoExiste('El usuario no existe en la base de datos.')
    except UsuarioNoExiste as e:
        print (f'Error: {e}') 

#muestra los usuarios adheridos a ese reclamo (aca se usa la tabla reclamos_usuarios )
def mostrar_usuarios_adheridos(p_id_reclamo:int) -> list:
    try:
        reclamo = db.session.query(ReclamoDB).filter_by(id=p_id_reclamo).first()
        # Verificar si se encontró el reclamo
        if reclamo:
            # Acceder a los reclamos adheridos por el usuario
            usuarios_adheridos = reclamo.usuarios_adheridos.all()
            # Iterar sobre los reclamos adheridos y obtener sus detalles
            lista=[]
            for usuario in usuarios_adheridos:
                lista.append(usuario.id)
            lista.sort()
            return print(lista)
        else:
            raise ReclamoNoExiste('El reclamo no existe en la base de datos.')
    except ReclamoNoExiste as e:
        print (f'Error: {e}') 