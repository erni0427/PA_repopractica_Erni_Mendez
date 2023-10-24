# Aplicación secundaria
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name)
from modules.gestorDB import GestorDB  # Importa tus clases
from modules.reclamo import Reclamo
from modules.departamento import DptoEspecifico, DptoTecnico
from modules.forms import RegisterForm, LoginForm

gestor = GestorDB()  # Instancia el gestor de reclamos

@app.route('/', methods=['GET', 'POST'])
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
    return render_template('registro.html', form=form)

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
            flash('Usuario o contraseña incorrectos', 'error')
    return render_template('login.html', form=form)
if __name__ == '__main__':
    app.run(debug=True)
