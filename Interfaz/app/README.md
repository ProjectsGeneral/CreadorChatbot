Create an environment Create a project folder and a .venv folder within:

LinuxWindows

mkdir myproject

cd myproject

py -3 -m venv .venv

Activate the environment Before you work on your project, activate the corresponding environment:

LinuxWindows

.venv\Scripts\activate

Your shell prompt will change to show the name of the activated environment.

Install Flask Within the activated environment, use the following command to install Flask:

pip install Flask
pip install flask-mysqldb
pip install flask-login
pip install flask-WTF
pip install bcrypt


Ejutar

python .\app\app.py


# DOCKER 

Instalar MySQL en Docker

1. https://www.docker.com/products/docker-desktop/
2. docker pull mysql
3. docker run --name mi_mysql -e MYSQL_ROOT_PASSWORD=chatbot -p 3306:3306 -d mysql
	Donde:
	mi_mysq -- es el nombre que le estás dando al contenedor.
	contraseña -- es la contraseña que deseas establecer para el usuario root de MySQL.
4. docker ps
	verifica que MySQL esté corriendo en Docker

-- OPCIONAL
5. docker exec -it mi_mysql mysql -u root -p
	Ejemplo de comando para conectarse al contenedor MySQL desde la línea de comandos y te pedirá la contraseña que estableciste anteriormente.

6. SHOW DATABASES;
7. USE nombre_de_la_base_de_datos;
8. SHOW TABLES;

------
Instalar PhpMyAdmin en Docker

1. docker pull phpmyadmin/phpmyadmin
2. docker run --name mi_phpmyadmin -d --link mi_mysql:db -p 8080:80 phpmyadmin/phpmyadmin
	Donde:
	mi_phpmyadmin -- es el nombre que le estás dando al contenedor phpMyAdmin.
	mi_mysql -- es el nombre del contenedor donde se está ejecutando MySQL.
	8080:80 mapea el puerto 8080 de tu sistema host al puerto 80 dentro del contenedor phpMyAdmin. Puedes cambiar el puerto según tus preferencias.

3. Acceder a phpMyAdmin: http://localhost:8080



POSIBLE BD


CREATE TABLE bots (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    saludo TEXT
);



CREATE TABLE palabras_clave_contenido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bot_id INT,
    clave VARCHAR(255) NOT NULL,
    contenido TEXT,
    FOREIGN KEY (bot_id) REFERENCES bots(id) ON DELETE CASCADE
);
