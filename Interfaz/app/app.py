from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_mysqldb import MySQL
from config import config
from controller.autenticacion import AuthController

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Solo para produccion

db = MySQL(app)
auth_controller = AuthController(db)

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

@app.route('/inicio')
def inicio():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user_name = session.get('user_name')
    user_email = session.get('user_email')
    
    return render_template('views/home.html', user_name=user_name, user_email=user_email)

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(debug=True, port=5000)
