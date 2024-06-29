from functools import wraps
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_mysqldb import MySQL
from config import config
from controller.autenticacion import AuthController
from controller.botController import BotController
from controller.userController import UserController

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Solo para produccion

db = MySQL(app)
auth_controller = AuthController(db)
bot_controller = BotController(db)
user_controller = UserController(db)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    return auth_controller.login(request)

@app.route('/registrarse', methods=['GET', 'POST'])
def registrarse():
    return auth_controller.register(request)

@app.route('/logout')
def logout():
    return auth_controller.logout()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/inicio')
@login_required
def inicio():
    user_name = session.get('user_name')
    user_email = session.get('user_email')
    return render_template('views/home.html', user_name=user_name, user_email=user_email)

@app.route('/listar-bots')
@login_required
def listarbots():
    user_name = session.get('user_name')
    user_email = session.get('user_email')
    
    bots = bot_controller.get_all_bots()
    
    return render_template('views/listar-bots.html', user_name=user_name, user_email=user_email, bots=bots)

@app.route('/eliminar-bot/<int:bot_id>', methods=['POST'])
@login_required
def eliminar_bot(bot_id):
    return bot_controller.eliminar_bot(bot_id)

@app.route('/editar-bot/<int:bot_id>', methods=['GET', 'POST'])
@login_required
def editar_bot(bot_id):
    if request.method == 'POST':
        return bot_controller.actualizar_datos_bot(bot_id)
    else:
        return bot_controller.mostrar_datos_bot_pclavesbot(bot_id)
    
@app.route('/ver-bot/<int:bot_id>', methods=['GET'])
@login_required
def ver_bot(bot_id):
    return bot_controller.mostrar_datos_completos(bot_id)

@app.route('/formulario', methods=['GET', 'POST'])
@login_required
def formulario():
    return bot_controller.create_bot(request)


@app.route('/perfil/<int:user_id>', methods=['GET', 'POST'])
@login_required
def perfil(user_id):
    if request.method == 'POST':
        return user_controller.editar_contraseña(request, user_id)
    else:
        return user_controller.mostrar_datos_usuario(user_id)



if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(debug=True, port=5000)
