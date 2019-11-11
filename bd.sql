CREATE DATABASE logear;

CREATE TABLE usuarios(
    id_usuario int(10) UNSIGNED primary key,
    usuario VARCHAR(100) NOT NULL,
    contrasenya VARCHAR(30) NOT NULL,
    activo tinyint(4) NOT NULL DEFAULT '1'
)