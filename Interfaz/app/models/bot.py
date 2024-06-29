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

    def create_bot(self, user_id, nombre, saludo, despliegue):
        try:
            cur = self.db.connection.cursor()
            cur.execute('INSERT INTO Bots (IdUsuario, Nombre, Saludo, Despliegue) VALUES (%s, %s, %s, %s)',
                        (user_id, nombre, saludo, despliegue))
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

    def get_bot_and_keywords_by_id(self, bot_id):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("""
                SELECT b.IdBot, b.IdUsuario, b.Nombre AS NombreBot, b.Saludo, b.Despliegue,
                    p.IdPClave, p.Clave, p.Contenido
                FROM Bots b
                LEFT JOIN PClaveBot p ON b.IdBot = p.IdBot
                WHERE b.IdBot = %s
            """, (bot_id,))
            bot_data = cursor.fetchall()

            if bot_data:
                bot = {
                    'IdBot': bot_data[0][0],
                    'IdUsuario': bot_data[0][1],
                    'Nombre': bot_data[0][2],
                    'Saludo': bot_data[0][3],
                    'Despliegue': bot_data[0][4],
                    'pclaves': []
                }

                for row in bot_data:
                    if row[5]:  
                        bot['pclaves'].append({
                            'IdPClave': row[5],
                            'Clave': row[6],
                            'Contenido': row[7]
                        })

                return bot
            else:
                return None

        except Exception as e:
            print(f"Error al obtener el bot {bot_id} y sus palabras clave: {str(e)}")
            return None
        finally:
            cursor.close()


    def update_bot_and_keywords(self, bot_id, nombre, saludo, pclaves_data, despliegue):
        try:
            cursor = self.db.connection.cursor()

            cursor.execute("""
                UPDATE Bots
                SET Nombre = %s, Saludo = %s, Despliegue = %s
                WHERE IdBot = %s
            """, (nombre, saludo, despliegue, bot_id))

            cursor.execute("""
                DELETE FROM PClaveBot
                WHERE IdBot = %s
            """, (bot_id,))

            for pclave in pclaves_data:
                cursor.execute("""
                    INSERT INTO PClaveBot (IdBot, Clave, Contenido)
                    VALUES (%s, %s, %s)
                """, (bot_id, pclave['Clave'], pclave['Contenido']))

            self.db.connection.commit()
            return True

        except Exception as e:
            print(f"Error al actualizar el bot y sus palabras clave: {str(e)}")
            self.db.connection.rollback()
            return False

        finally:
            cursor.close()
