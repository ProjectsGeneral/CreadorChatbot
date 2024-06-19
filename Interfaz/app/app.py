from flask import Flask, render_template, request, url_for, redirect,request,flash
from flask_mysqldb import MySQL

from config import config

app = Flask(__name__)

db = MySQL(app)


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    data = {
        'titulo':'Iniciar Sesion',
        'Correo':'Correo electronico',
        'Password':'Contraseña',
        'InngresaCorreo':'Ingresa tu Correo electronico',
        'IngresaPassword':'Ingresa tu Contraseña',
    }
    return render_template('security/login.html', data=data)
    
    

@app.route('/registrarse')
def registrarse():
    data = {
        'titulo':'Registrate',
        'Nombre':'Nombre',
        'Apellidos':'Apellidos',
        'Correo':'Correo electronico',
        'Empresa': 'Nombre de la Empresa',
        'Cargo': 'Ingresa su cargo',
        'Password':'Contraseña',
        'PasswordRepeat':'Repite la Contraseña',
        
    }
    return render_template('security/register.html',data=data)

@app.route('/validar')
def validar():
    data = {
        'titulo':'Ingresa un correo electronico valido',
        'Correo':'Correo electronico',
        'Codigo':'Codigo',
    }
    return render_template('security/validate.html',data=data)

@app.route('/recuperar/<dataCorreo>')
def recuperar(dataCorreo):
    data = {
        'titulo':'Recuperar Contraseña',
        'Correo':'Correo electronico',
        'dataCorreo': dataCorreo,
        'Password':'Ingresa una nueva contraseña',
    }
    return render_template('security/recover.html',data=data)



@app.route('/inicio')
def inicio():
    return render_template('views/home.html')




@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data = {
        'nombre': nombre,
        'apellido':'Chambilla',
        'edad' : edad
    }
    return render_template('contacto.html', data=data)

# recuperar parametro a traves de una url
def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return "ok"

def pagina_no_encontrada(error):
    # return render_template('404.html'), 404
    return redirect(url_for('index'))





if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True,port=5000)


# antes de la peticion
# @app.before_request
# def before_request():
#     print("Antes de la peticion..")

# despues de la peticion
# @app.after_request
# def after_request(response):
#     print("Despues de la peticion..")
#     return response 