# Variabnles
# ******************

nombre = 'Pedro'

print(nombre)

# Calcular el area de un circulo

pi = 4.1415
radio = 3

# Calculo. Para elevar a la potencia ponemos "**"

area = pi * radio**2

print(area)

# Nombre y apellido

nombre2 = 'Pedro'
apellido = 'Fernandez'

# Entrada de datos
# raw_input: Nos permite poner un input en donde en la consola nos permtira colocar el dato. Funciona en la version 2, en la version 3 se llama "input"
# "+" EN STRING: Sirve para concatenar cadeans de string
# str(): Nos permite indicarle a una funcion o lo que tengamos que es tipo STRING
# int(): Nos permite indicarle a una funcion o lo que tengamos que es tipo STRING
# tipoDato(): Nos permite indicarle a una funcion o lo que tengamos segun el tipo de dato (string, float, int, etc.)
# IMPORTANTE: NO habria problema si no pusieramos en input, str. ya que al tener ene l print "+" para concatenar, convierte automaticamente lo que pongamos
# en el input en STRING, el problema viene si ponemos en vez de str() un int(). NOs daria error porque el input tipo INT() no soporta los "+" que pusimos para concatenar strings
# ya que precisamente los usamos para concatenar STRINGS.

# nombre3 = input('Cual es tu nombre?')

# print('Hola ' + nombre + ' Un gusto en conocerte')

# Prioridades de Operadores GENERICOs: Caracteres que tienen prioridad segun lo que la consola leera.
# 1. ()
# 2. **
# 3. *, /, mod, not
# 4. +, -, and
# 5. >, <, ==, >=, <=, !=, or

# OPERADORES DE ASIGNACION: sIRVEN PARA ASIGNAR UN VALOR
# =
# +=, -=, *=, /=, **=, %=

# Concatenar con STRINg y variables

# CONCATENADO GENERICO: "," lA COMA nos permite concatenar variables, string o enteros. Ademas la coma hace la misma funcion de espacio " ".

nombre4 = 'Pedro'
altura = 1.86

# Primera Opcion

print('Hola me llamo',nombre,'y mido',altura,'metros de estatura')
# Segunda Opcion
# En esta opcion solo necesitamos unpar de comillas
# FORMAT(variable1, variable2): Nos permite

# print('Hola me llamo {} y mido {} metros de estatura').format(nombre,altura)

# Tercera Opcion
# print(f 'string {variable}'): la F es formar pero en una forma mas rapida
# IMPORTANTE: SI TENEMOS EL PRINT MUY LARGO, PYTHON nos dara error si damos intro, ya que es sencible.
# parta solucionarlo cerramos y abrimos las comillas de string cada vez que damos intro.

print(f'Hola me llamo {nombre} y mido {altura} metros de estatura')

# Entrada de datos
# Input te guarda datos tipo cadena

nombre5 = input('tu nombre: ')

#input guardar valoees numericos

edad = int(input('Tu edad: '))

altura = float(input('Tu altura: '))

print(f'Hola tu {nombre5} y tu edad es {edad}, como tu altura {altura}')

# Convertir un string en entero
# Usamos las funciones de tipos de datos, tipoDAto(), ten en cuenta en que el string debe tener el tipo de dato para que la funcion lo aplique
# es decir, no vas a poner un 'Hola' en un int, sabiendo que no va funcionar sino por ejemplo '10'

n = int('10')
print(n)
# COnvertir un numero a binario

n = bin(10)
print(n)
# Convertir un numero a hexadecimal

n = hex(10)
print(n)
# Convertir un binario a un entero
# el 2 nos permite indicartle que es binario

n = int('0b1010', 2)
print(n)
# Convertir un hexadecimal a entero
# el 16 nos permite indicartle que es hexagecimal

n = int('0xa', 16)
print(n)
# Convertir un negativo en positivo

n = abs(-12)
print(n)
# Convertir de numero decimal a entero

n = round(4.8)
print(n)
# Cuenta Cantidad de Caracteres

n = len('Toni')
print(n)


