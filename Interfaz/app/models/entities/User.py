from werkzeug.security import check_password_hash 
from flask_login import UserMixin
#generate_password_hash

class LoginUser(UserMixin):

    def __init__(self,id,Correo,Password,Nombre="",Apellidos="",NombreEmpresa="",Cargo="",RepeatPassword="") -> None:
        self.id = id
        self.Nombre = Nombre
        self.Aapellido = Apellidos
        self.Correo = Correo
        self.NombreEmpresa = NombreEmpresa
        self.Cargo = Cargo
        self.Password = Password
        self.RepeatPassword = RepeatPassword

    @classmethod
    def check_password(self, hashed_password, Password):
        return check_password_hash(hashed_password, Password)

