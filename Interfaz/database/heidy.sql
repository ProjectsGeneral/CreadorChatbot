CREATE TABLE Usuario (
    IdUsuario INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(30) NOT NULL,
    Apellidos VARCHAR(40) NOT NULL,
    Correo VARCHAR(40) NOT NULL,
    NombreEmpresa VARCHAR(40) NOT NULL,
    Cargo VARCHAR(30) NOT NULL,
    Password VARCHAR(100) NOT NULL
);

-- Creación de la tabla Bots
CREATE TABLE Bots (
    IdBot INT PRIMARY KEY AUTO_INCREMENT,
    IdUsuario INT NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Saludo TEXT NOT NULL,
    Despliegue VARCHAR(50) NOT NULL,
    Puerto INT NOT NULL,
    CONSTRAINT fk_IdUsuario FOREIGN KEY (IdUsuario) REFERENCES Usuario(IdUsuario)
);

-- Creación de la tabla PClaveBot
CREATE TABLE PClaveBot (
    IdPClave INT PRIMARY KEY AUTO_INCREMENT,
    IdBot INT NOT NULL,
    Clave VARCHAR(50) NOT NULL,
    Contenido TEXT NOT NULL,
    CONSTRAINT fk_IdBot FOREIGN KEY (IdBot) REFERENCES Bots(IdBot)