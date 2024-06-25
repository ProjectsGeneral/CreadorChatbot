from flask import session, flash, redirect, url_for, render_template, request
from models.bot import Bot
from models.pclavebot import PClaveBot
import logging

class BotController:
    def __init__(self, db):
        self.bot_model = Bot(db)
        self.pclave_model = PClaveBot(db)
        self.logger = logging.getLogger(__name__)  

    def get_all_bots(self):
        return self.bot_model.get_all_bots()

    def create_bot(self, request):
        if request.method == 'POST':
            nombre = request.form.get('nombre')
            saludo = request.form.get('saludo')
            user_id = session.get('user_id')

            try:
                bot_id = self.bot_model.create_bot(user_id, nombre, saludo)
                if not bot_id:
                    raise Exception('Error al crear el bot en la base de datos')

                keywords = []
                for key, value in request.form.items():
                    if key.startswith('clave') and value.strip():
                        index = key[len('clave'):]
                        contenido_key = f'contenido{index}'
                        if contenido_key in request.form:
                            keywords.append({'clave': value, 'contenido': request.form.get(contenido_key)})

                for keyword in keywords:
                    clave = keyword['clave']
                    contenido = keyword['contenido']
                    pclave_id = self.pclave_model.create_pclave(bot_id, clave, contenido)
                    if not pclave_id:
                        raise Exception(f'Error al crear la palabra clave "{clave}" para el bot ID {bot_id}')

                flash('¡Bot creado exitosamente!', 'success')
                return redirect(url_for('formulario'))

            except Exception as e:
                error_message = 'Hubo un problema durante la creación del bot'
                flash(error_message, 'danger')
                self.logger.error(f'{error_message}: {str(e)}')
                return redirect(url_for('formulario'))

        data = {
            'Nombre': 'Nombre del Bot',
            'Saludo': 'Saludo del Bot',
            'Clave': 'Palabra Clave',
            'Contenido': 'Contenido de la Palabra Clave',
        }
        return render_template('views/form.html', data=data)
