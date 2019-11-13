CREATE DATABASE ahorcadito;

CREATE TABLE palabras(
    id_palabra int(10) UNSIGNED primary key auto_increment,
    palabra VARCHAR(100) NOT NULL
)

CREATE TABLE usuarios(
    id_usuario int(10) auto_increment,
    usuario VARCHAR(100) NOT NULL,
    contrasenya VARCHAR(30),
    activo tinyint(4) NOT NULL DEFAULT '1',
    PRIMARY KEY (id_usuario)
);

CREATE TABLE puntuacion(
    id_puntuacion int(10) auto_increment,
    id_usuario int(10),
    record int(100),
    aciertos int(100),
    fallos int(100),
    PRIMARY KEY (id_puntuacion),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);