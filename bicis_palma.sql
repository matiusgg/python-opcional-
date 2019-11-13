CREATE TABLE IF NOT EXISTS cliente(
    -- PK DE LA TABLA /
    -- ID_cliente , INTEGER UNSIGNED PRIMARY KEY AUTO-INCREMENT,
    dni INTEGER UNSIGNED PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    apellidos VARCHAR(40) NOT NULL,
    direccion VARCHAR(100) NOT NULL, 
    poblacion VARCHAR(20) NOT NULL DEFAULT 'Palma',
    Codpostal VARCHAR(5) NOT NULL,
    Telefono VARCHAR(15) NOT NULL,
    fNacimiento DATETIME NOT NULL,
    email VARCHAR(40) NOT NULL UNIQUE,
    fechaAlta TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    faltas ENUM('*', '**', '***') 
);
CREATE TABLE tarifa(
    ID_tarifa INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    tipoSevicio ENUM('max30', 'max60', 'max24h') NOT NULL,
    duracion VARCHAR(3) NOT NULL, 
    precio DOUBLE(6,2) NOT NULL DEFAULT 10.50
);
CREATE TABLE inventario(
    -- PK DE LA TABLA /
    ID_bicicleta INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    modelo VARCHAR(15),
    estado ENUM('uso', 'reparacion', 'disponible', 'baja') NOT NULL,
    color VARCHAR(20) NOT NULL,
    fAlta TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fBaja DATETIME,
    descripcion TEXT
    -- En descripcion se pone el tipo de libro: genero y sipnosis
);
CREATE TABLE reparacion (
    ID_reparacion INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    fEntrega DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fRecogida TIMESTAMP,
    precio DOUBLE(6,2) DEFAULT 10.50 NOT NULL,
    empresaReparaciones ENUM('esta', 'laotra', 'aquella'),
    descripcion TEXT
);

CREATE TABLE empresasReparacion (
    ID_Ereparacion INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nEmpresa VARCHAR(20) NOT NULL,
    apellidos VARCHAR(40) NOT NULL,
    direccion VARCHAR(100) NOT NULL, 
    poblacion VARCHAR(20) NOT NULL DEFAULT 'Palma',
    Codpostal VARCHAR(5) NOT NULL,
    Telefono VARCHAR(15) NOT NULL,
    Especialidad VARCHAR(15),
    email VARCHAR(40) NOT NULL UNIQUE,
    fAlta TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Fecha en la que inicamos con la empresa',
    descripcion TEXT
);
