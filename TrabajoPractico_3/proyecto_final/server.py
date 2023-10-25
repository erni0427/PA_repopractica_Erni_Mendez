from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
from modules.gestorBD import GestorBD  # Importa tus clases
from modules.reclamo import Reclamo
from modules.departamento import DptoEspecifico, DptoTecnico
from modules.usuario import Usuario_Final,Secretario_Tecnico, Jefe_Dpto
from modules.forms import RegisterForm, LoginForm
gestor = GestorBD("mi_base_de_datos")# Instancia el gestor de reclamos
  
@app.route("/", methods=['GET', 'POST'])
def home():    
    if len(gestor) == 0:
        return render_template("home.html", esta_vacia=True)
    else:
        return render_template("home.html", esta_vacia=False, lista_libros=gestor )

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Lógica de inicio de sesión
        # Verifica si el usuario y la contraseña son válidos
        email = form.email.data
        contrasena = form.password.data
        usuario = gestor.iniciar_sesion(email, contrasena)
        if usuario:
            # Usuario autenticado, realiza la lógica de redirección
            return redirect(url_for('dashboard'))
        else:
            raise('Usuario o contraseña incorrectos', 'error')
    return render_template('login_register.html', form=form, title='Iniciar Sesión')


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegisterForm()
    if form.validate_on_submit():
        # Obtén los datos del formulario
        nombre = form.nombre.data
        apellido = form.apellido.data
        email = form.email.data
        nombre_usuario = form.username.data
        claustro = form.claustro.data
        contrasena = form.password.data
        
        # Crea un objeto de usuario y regístralo en la base de datos
        usuario = Usuario_Final(nombre_usuario, gestor.obtener_nuevo_id_usuario(), nombre, apellido, email, claustro, contrasena)
        gestor.registrar_usuario(usuario)
        return redirect(url_for('login'))
    return render_template('login_register.html', form=form, title='Registro')
    
if __name__ == '__main__':
    app.run(debug=True)



    # def lectura_formulario_user(self,register_form):
    #     dic={}
    #     if UsuarioDB.query.filter_by(email=register_form.email.data).first():
    #         raise UsuarioYaExiste('El usuario ya existe en la base de datos')

    #     encripted_pass = generate_password_hash(
    #         password=register_form.password.data,
    #         method='pbkdf2:sha256',
    #         salt_length=8
    #     )
    #     dic['email']=register_form.email.data,
    #     dic['password']=encripted_pass,
    #     dic['user_name']=register_form.username.data,
    #     dic['lastname']=register_form.apellido.data,
    #     dic['name']=register_form.nombre.data,
    #     dic['claustro']=register_form.claustro.data
    #     return dic
    
    # def lectura_formulario_reclamo(self,reclamo_form):
    #     dic={}
    #     #Obtén los datos del formulario de reclamo
    #     dic['titulo'] = reclamo_form.titulo.data
    #     dic['descripcion'] = reclamo_form.descripcion.data
    #     dic['fecha_creacion'] = datetime.now()  # Asigna la fecha actual
    #     #usuario_id se pasa como argumento al método para vincular el reclamo al usuario que lo crea
    #     return dic