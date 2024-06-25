from functools import wraps
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_mysqldb import MySQL
from config import config
from controller.autenticacion import AuthController
from controller.bot import BotController

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Solo para produccion

db = MySQL(app)
auth_controller = AuthController(db)
bot_controller = BotController(db)

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

@app.route('/validar')
def validar():
    data = {
        'titulo':'Ingresa un correo electronico valido',
        'Correo':'Correo electronico',
        'Codigo':'Codigo',
    }
    return render_template('security/validate.html',data=data)

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
    
    # Obtener todos los bots utilizando el controlador BotController
    bots = bot_controller.get_all_bots()
    
    return render_template('views/listar-bots.html', user_name=user_name, user_email=user_email, bots=bots)

@app.route('/formulario', methods=['GET', 'POST'])
@login_required
def formulario():
    return bot_controller.create_bot(request)

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(debug=True, port=5000)
