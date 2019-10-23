<?php
/*
Abrir y cerrar archivos de testo desde PHP
*/
//primero abrimos el archivo paa poder manipularlo con fopen()
//
$archivo= fopen('archivo.txt','r');
//leer la primera linea del archivo
$contenido=fgets($archivo);
echo $contenido;



?>