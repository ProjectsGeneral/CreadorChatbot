from flask import current_app, session, flash, redirect, url_for, render_template, request
import requests
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
                api_url = 'https://random-word-api.herokuapp.com/word'
                response = requests.get(api_url)
                random_word = response.json()[0] 

                despliegue = random_word

                bot_id = self.bot_model.create_bot(user_id, nombre, saludo, despliegue)
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

            except requests.RequestException as e:
                error_message = f'Error al obtener la palabra aleatoria desde la API: {str(e)}'
                flash(error_message, 'danger')
                self.logger.error(error_message)
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
    
    def eliminar_bot(self, bot_id):
        try:
            success_keywords = self.pclave_model.delete_pclaves_by_bot(bot_id)
            if not success_keywords:
                raise Exception('Error al eliminar las palabras clave del bot')

            success_bot = self.bot_model.delete_bot(bot_id)
            if not success_bot:
                raise Exception('Error al eliminar el bot principal')

            flash('¡Bot eliminado exitosamente!', 'success')
            return redirect(url_for('listarbots'))

        except Exception as e:
            error_message = 'Hubo un problema al intentar eliminar el bot'
            flash(error_message, 'danger')
            self.logger.error(f'{error_message}: {str(e)}')
            return redirect(url_for('listarbots'))
        
        
    def mostrar_datos_bot_pclavesbot(self, bot_id):
        try:
            bot_data = self.bot_model.get_bot_and_keywords_by_id(bot_id)
            if not bot_data:
                flash(f'No se encontró el bot con ID {bot_id}', 'danger')
                return redirect(url_for('listarbots'))

            return render_template('views/editar-bot.html', data=bot_data)

        except Exception as e:
            error_message = f'Hubo un problema al intentar mostrar los datos del bot ID {bot_id}: {str(e)}'
            flash(error_message, 'danger')
            return redirect(url_for('listarbots'))
        
    def mostrar_datos_completos(self, bot_id):
        try:
            bot_data = self.bot_model.get_bot_and_keywords_by_id(bot_id)
            if not bot_data:
                flash(f'No se encontró el bot con ID {bot_id}', 'danger')
                return redirect(url_for('listarbots'))

            return render_template('views/info-completo-bot.html', data=bot_data)

        except Exception as e:
            error_message = f'Hubo un problema al intentar mostrar los datos del bot ID {bot_id}: {str(e)}'
            flash(error_message, 'danger')
            return redirect(url_for('listarbots'))
        
    def actualizar_datos_bot(self, bot_id):
        try:
            nombre = request.form.get('nombre')
            saludo = request.form.get('saludo')

            palabras_clave = []
            contenidos = []
            for key in request.form.keys():
                if key.startswith('clave_'):
                    palabras_clave.append(request.form.get(key))
                elif key.startswith('contenido_'):
                    contenidos.append(request.form.get(key))

            if len(palabras_clave) != len(contenidos):
                flash('Error al procesar las palabras clave y contenidos', 'danger')
                return redirect(url_for('editar_bot', bot_id=bot_id))

            pclaves_data = [{'Clave': pc, 'Contenido': co} for pc, co in zip(palabras_clave, contenidos)]

            api_url = 'https://random-word-api.herokuapp.com/word'
            response = requests.get(api_url)
            random_word = response.json()[0]

            despliegue = random_word 

            success = self.bot_model.update_bot_and_keywords(bot_id, nombre, saludo, pclaves_data, despliegue)

            if success:
                flash('Bot actualizado con éxito', 'success')
                return redirect(url_for('listarbots', bot_id=bot_id))
            else:
                flash('Error al actualizar el bot', 'danger')
                return redirect(url_for('editar_bot', bot_id=bot_id))

        except Exception as e:
            flash(f'Error al actualizar el bot: {e}', 'danger')
            return redirect(url_for('editar_bot', bot_id=bot_id))
    


