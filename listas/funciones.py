'''
FUNCIONES
def/return
DEf: Para definir una funcion, es decir en PHP por ejemplo pon emos function para espceficiar que es una funcion
aqui en vez de function usamos DEF
'''

# definimos una funcion por parametro
# Tambien aplica la TABULACION JERARQUIA

def suma(num1, num2):
# RETURN pasra que nos devuelva el valor
    return num1 + num2

suma(3,5)

print(suma(3,5))

# tortuga con FUNCIONES

import turtle


# Activacion de la ventana dibujo
# Oceano() esta llamando a la funcion haz_rectangulo

def oceano():
# window: se encarga de abrir la ventana
    window = turtle.Screen
    tortuguita = turtle.Turtle()

    haz_rectangulo(tortuguita)
    turtle.mainloop()



# haz_rectangulo se encarga de poner el largo y alto del cuadrado
# esta llamando a las funciones de haz_linea y haz_alto
def haz_rectangulo(tortuguita):
    largo = float(input('Largo: '))
    alto = float(input('Alto: '))

# RANGE: que permita que las
    for i in range(2):
        
        haz_linea(tortuguita, largo)
        haz_alto(tortuguita, alto)


def haz_linea(tortuguita, largo):
    #el paarametro tortuguita es el tortuguita del tortuguita. simplemeten cuando en el paramreto colocamos
    # la variable de la funcion ocean() de tortuguita, estas dos gunciones se ejecutan correctamente
    tortuguita.forward(largo)
    # para que siempre haga un angulo de 90 grados en el rectangulo
    tortuguita.left(90)

def haz_alto(tortuguita, alto):
    tortuguita.forward(alto)
    tortuguita.left(90)


# Donde comenzara nuestro codigo usaremos, es decir con __name__ le estamos indicando que aunque 
# el anterior codigo antes de colocar este if con __name__ se guarda en memoria, no lo esta ejecutando
# hasta que se lo indiquemos con __name__. Por lo cual con __name__ le decimos que ejecute ese codigo que le ponemos
# esto nos evite errores que no queremos solo por tener las funciones que se ejecutan sin que nosotros le indiquemos
# con __name podemos indicarle que cominece a ejecutar ese codigo que queremos

if __name__ == '__main__':

    # En este caso que ejecute el oceano(), que tiene las demas funciones

    oceano()

