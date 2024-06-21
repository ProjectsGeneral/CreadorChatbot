from flask import session, flash, redirect, url_for, render_template
import bcrypt
from models.user import User

class AuthController:
    def __init__(self, mysql):
        self.user_model = User(mysql)

    def login(self, request):
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            user = self.user_model.get_user_by_email(email)
            if user and bcrypt.checkpw(password.encode('utf-8'), user['Password'].encode('utf-8')):
                session['user_id'] = user['IdUsuario']
                session['user_name'] = user['Nombre']
                session['user_email'] = user['Correo']
                flash('¡Inicio de sesión exitoso!', 'success')
                return redirect(url_for('inicio'))
            else:
                flash('Correo o contraseña inválidos', 'danger')
                return redirect(url_for('login'))

        data = {
            'titulo': 'Iniciar Sesión',
            'Correo': 'Correo electrónico',
            'Password': 'Contraseña',
            'InngresaCorreo': 'Ingresa tu Correo electrónico',
            'IngresaPassword': 'Ingresa tu Contraseña',
        }
        return render_template('security/login.html', data=data)

    def register(self, request):
        if request.method == 'POST':
            nombre = request.form['nombre']
            apellidos = request.form['apellidos']
            correo = request.form['correo']
            empresa = request.form['empresa']
            cargo = request.form['cargo']
            password = request.form['password']

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            
            if self.user_model.get_user_by_email(correo):
                flash('El correo electrónico ya está registrado', 'danger')
                return redirect(url_for('registrarse'))

            user_id = self.user_model.create_user(nombre, apellidos, correo, empresa, cargo, hashed_password)
            if user_id:
                flash('¡Registro exitoso! Por favor, inicia sesión', 'success')
                return redirect(url_for('login'))
            else:
                flash('Hubo un problema durante el registro', 'danger')
                return redirect(url_for('registrarse'))

        data = {
            'titulo': 'Regístrate',
            'Nombre': 'Nombre',
            'Apellidos': 'Apellidos',
            'Correo': 'Correo electrónico',
            'Empresa': 'Nombre de la Empresa',
            'Cargo': 'Ingresa su cargo',
            'Password': 'Contraseña',
        }
        return render_template('security/register.html', data=data)

    def logout(self):
        session.clear()
        flash('¡Has cerrado sesión correctamente!', 'success')
        return redirect(url_for('login'))
    

