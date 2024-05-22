from .entities.User import LoginUser

class ModelLoginUser():

    @classmethod
    def login(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, Correo, Password FROM Usuario WHERE Correo = '{}'""".format(usuario.Correo)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is not None:
                usuario = LoginUser(row[0], row[1], LoginUser.check_password(row[2], usuario.Password))
                return usuario
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
 
    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, Correo, Nombre, NombreEmpresa FROM Usuario 
                    WHERE id = {}""".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is not None:
                return LoginUser(row[0], row[1], None, row[2],None, row[3])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)