from flask_mysqldb import MySQLdb

class User:
    def __init__(self, db):
        self.db = db

    def get_user_by_email(self, email):
        cur = self.db.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('SELECT * FROM Usuario WHERE Correo = %s', (email,))
        user = cur.fetchone()
        cur.close()
        return user if user else None

    def create_user(self, name, last_name, email, company_name, position, password):
        try:
            cur = self.db.connection.cursor()
            cur.execute('INSERT INTO Usuario (Nombre, Apellidos, Correo, NombreEmpresa, Cargo, Password) VALUES (%s, %s, %s, %s, %s, %s)',
                        (name, last_name, email, company_name, position, password))
            user_id = cur.lastrowid  
            self.db.connection.commit()
            cur.close()
            return user_id  
        except Exception as e:
            self.db.connection.rollback()  
            print(f"Error en la inserción del usuario: {str(e)}")
            return None 
        
    def get_user_by_id(self, user_id):
        cur = self.db.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('SELECT * FROM Usuario WHERE IdUsuario = %s', (user_id,))
        user = cur.fetchone()
        cur.close()
        return user if user else None
    
    def update_user_password(self, user_id, new_password):
        try:
            cur = self.db.connection.cursor()
            cur.execute('UPDATE Usuario SET Password = %s WHERE IdUsuario = %s',
                        (new_password, user_id))
            self.db.connection.commit()
            cur.close()
            return True
        except Exception as e:
            self.db.connection.rollback()
            print(f"Error al actualizar la contraseña del usuario: {str(e)}")
            return False