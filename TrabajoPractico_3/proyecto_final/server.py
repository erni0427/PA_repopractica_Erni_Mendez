
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