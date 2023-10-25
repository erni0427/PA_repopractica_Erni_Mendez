from modules.usuario import Usuario, Usuario_Final, Secretario_Tecnico, Jefe_Dpto

class GestorUsuarios:
    def __init__(self, uf=Usuario_Final, st=Secretario_Tecnico, jd=Jefe_Dpto):
        self.__usuariosfinales=uf
        self.__secretarios=st
        self.__jefes=jd
    
    @property
    def usuariosfinales(self):
        return self.__usuariosfinales
    
    @property
    def secretarios(self):
        return self.__secretarios
    
    @property
    def jefes(self):
        return self.__jefes
    
    # def registrar_usuariof(self, uf):
    # # Comprobar si el nombre de usuario o correo ya existen
    # if any(u.nombre_usuario == uf.nombre_usuario or u.id_usuario == uf.id_usuario for u in self.usuariosfinales):
    #     print("Nombre de usuario o correo electrónico ya existen. Por favor, elija otro.")
    #     return False

    # self.usuarios.append(usuario)
    # print("Usuario registrado exitosamente.")
    # return True

