'''
DIFERENCIAS ENTRE PYTHON 2 Y PYTHON 3.

Si entramos a python 2. 
1. DIFERENCIA: En python 2 no tenemos un print(), es decir no era una funcion sino una propiedad: print 'Hola'
2. Cuando se hagan operaciones en python 2, y estas operaciones el resultado da con decimales, python 2 no te los da con decimales,
en cambio pthon 3 si.
3. En python 2 no teniamos la tabla unicode
4. Hay muchas librerias que siguen estando en python 2, por lo cual si hay proyectos de hace años con estas librerias
no vendran problemas si ya queremos usarlas con python 3, auqnue muchas ya estan en python 3, otrasd no por lo cual, hay que mirar otras similares o crearlas nosotros mismos.
5. INPUT: En python 2, se escribia: raw_input. mientras en python 3, solamente es poner input()
6. Si estamos en un entorno que obliga a que trabajeros con python 2, lo que nos tocara es que descargemos python 2, para configurarlo a python 3

'''

'''
COMO SE GUARDFA LA INFORMACION EN DISCO DE UNA APLICACION EN PYTHON
Creamos un archivo txt con en php y para usarlo como en php, tenemos que tener en cuenta:

W: escribir en el archivo, pero te pisa el contenido que tengas previamente
R: leer
A: escribir al final, no te pisa el contenido anterior
r+: lee y escribe
'''
# ejemplo
nombre = input('Nombre: ')

# Escritura

# WITH: Nos permite encajar todo el contenido dentro de un 'espacio'. Es un tema de comodidad
# REcordemos que con open(), nos permite abrir el archivo y la opcion que queramos, pero si no encuentra el archivo lo crea

with open('file.txt', 'a') as f:

    for i in range(5):
        f.write(f'{nombre}\n')
    f.close()

# o tambien:

# f = open ('file.txt', 'w')
# f.write(nombre, '\n')
# f.close

# Lectura

with open('file.txt', 'r') as f:

    for linea in f:
        print(linea)