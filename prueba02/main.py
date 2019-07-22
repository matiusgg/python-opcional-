'''

# PASS: Si delcaro una funcion/condicional/bucle pero no queremos todavia ontrudcirle codigo, usamos PASS para que pase de ella
# y no nos de error si lo dejamos vacio.


MAIN: 

Evutar poner -*- coding: utf-8 -*-. Ya que es antiguo

ACSII / UNICODE: La diferencia es que ASCSII esta en 160(tabla creada por EEUU para asignar numeros binarios a caracteres)
En cambio, UNICODE se establecen todos los codigos ya universales, ya que en la version python 2, esta el ASCII, en cambio,
python 3 esta UNICODE. Por l cual tener cuidado en que versione stamos
'''

# def cosa():
#     print('cosa')

'''
Si quitamos el if main y dejamos el codigo en la tabulacion que tenia, nos hara un bucle
'''


# INICIO DEL PROGRAMA: MAIN nos permite hscer una lectura inicial de todo en memoria de arriba hacia abajo, y luego viene hasta el if main a ejecutar el programa
# ESta encapsulando toda la informacion, MAIN es un inicio del programa de PYTHON
# if __name__ == "__main__":
#     print('Ejecuntando principal')
#     cosa()


# CALCULADORA DE DIVISAS: que nos haga las LIBRAs -> euros

# Funciones qu epondramos en el MAIN. En las funciones da completamente igual si el codigo se crea antes o despues, ya que al cargars en memoria
# con el MAIN no da problemas

def inicio():

    pregunta = float(input('Que conversion quieres? 1.libra 2.euros: '))

    if pregunta == 1:
        libra()

    if pregunta == 2:
        euro()
    
    else:
        print('No has escogido una opcion')


def libra():

    dinero = float(input('Introduce la cantidad de libra -> euro:'))

    if dinero != 0:
        dinero *= 1.1125
        print(f'Conversion a euros es: {dinero:.2f}')


def euro():

    dinero = float(input('Introduce la cantidad de euro -> libra:'))

    if dinero != 0:
        dinero *= 0.90
        print(f'Conversion a libras es: {dinero:.2f}')



# Ahora hacemos el MAIN, para dar a entender el inicio del codigo

if __name__ == "__main__":
    inicio()