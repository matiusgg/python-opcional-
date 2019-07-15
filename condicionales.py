'''
CONDICIONALES
IF
":"= Los dos puntos significan continuacion, es decir como abrir {}. 
Al no haber [] {} entonces la tabulacion y los espacios se tiene muy encuentA

ELIF: es ELSE IF.
'''
# if 10 >0:
#     print('esto es un if')
#     print('otra linea')

# elif 10 == 0:
#     print('Esto se parece a else if')
# else:
#     print('esto es un else')

# edad = int(input('Cual es tu edad: '))

# if edad >= 0 and edad <= 120:
#     print('La introducicon de datos es correcta')
#     if edad >= 18:
#         print('Eres mayor de edad')
#     if edad < 18: 
#         print('Eres un menor de edad')
# else:
#     print('Te has equivocado con la introduccion de edad')


# Pedir a 3 personas la edad, de ellas nos quedamos con el que mas tiene edad

# Datos
# persona1 = str(input('Cual es tu nombre persona1?: '))
# edad1 = int(input(f'Cual es tu edad {persona1}?: '))
# persona2 = str(input('Cual es tu nombre persona2: '))
# edad2 = int(input(f'Cual es tu edad {persona2}?: '))
# persona3 = str(input('Cual es tu nombre persona3: '))
# edad3 = int(input(f'Cual es tu edad {persona3}?: '))

# if edad1 > edad2 and edad1 > edad3:
#     per1per2 = edad1 - edad2
#     per1per3 = edad1 - edad3
#     print(f'Tu {persona1} eres el mayor, con la diferencia de {per1per2} a {persona2} y {per1per3} a {persona3}')


# if edad2 > edad1 and edad2 > edad3:
#     per2per1 = edad2 - edad1
#     per2per3 = edad2 - edad3
#     print(f'Tu {persona2} eres el mayor, con la diferencia de {per2per1} a {persona1} y {per2per3} a {persona3}')


# if edad3 > edad2 and edad3 > edad1:
#     per3per2 = edad3 - edad2
#     per3per1 = edad3 - edad1
#     print(f'Tu {persona3} eres el mayor, con la diferencia de {per3per2} a {persona2} y {per3per1} a {persona1}')

# lower(): Le indicamos que obligatoriamente lo que pongamos en el input se ponga todo en minusculas

caracter = input('Insertar una letra').lower()

if caracter == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':

    print('Es una vocal')
else:
    print('No es una vocal')