from flask_mysqldb import MySQLdb

class PClaveBot:
    def __init__(self, db):
        self.db = db

    def create_pclave(self, bot_id, clave, contenido):
        try:
            cur = self.db.connection.cursor()
            cur.execute('INSERT INTO PClaveBot (IdBot, Clave, Contenido) VALUES (%s, %s, %s)',
                        (bot_id, clave, contenido))
            pclave_id = cur.lastrowid
            self.db.connection.commit()
            cur.close()
            return pclave_id
        except Exception as e:
            self.db.connection.rollback()
            print(f"Error en la inserción de la palabra clave del bot: {str(e)}")
            return None
