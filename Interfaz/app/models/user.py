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
            user_id = cur.lastrowid  # Obtiene el ID del usuario insertado
            self.db.connection.commit()
            cur.close()
            return user_id  # Devuelve el ID del usuario insertado
        except Exception as e:
            self.db.connection.rollback()  
            print(f"Error en la inserción del usuario: {str(e)}")
            return None 
