from flask_mysqldb import MySQLdb

class Bot:
    def __init__(self, db):
        self.db = db

    def get_all_bots(self):
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT * FROM Bots")
        bots = cursor.fetchall()
        cursor.close()
        return bots

    def create_bot(self, user_id, nombre, saludo):
        try:
            cur = self.db.connection.cursor()
            cur.execute('INSERT INTO Bots (IdUsuario, Nombre, Saludo) VALUES (%s, %s, %s)',
                        (user_id, nombre, saludo))
            bot_id = cur.lastrowid
            self.db.connection.commit()
            cur.close()
            return bot_id
        except Exception as e:
            self.db.connection.rollback()
            print(f"Error en la inserción del bot: {str(e)}")
            return None
    
    def delete_bot(self, bot_id):
        try:
            cur = self.db.connection.cursor()
            cur.execute('DELETE FROM Bots WHERE IdBot = %s', (bot_id,))
            self.db.connection.commit()
            cur.close()
            return True
        except Exception as e:
            self.db.connection.rollback()
            print(f"Error al eliminar el bot {bot_id}: {str(e)}")
            return False


