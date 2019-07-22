'''
NUMEROS PRIMOS: Divisores por 1 y por ellos mismos
Tabla de Numeros Primos con 2
el usuario nos inserta un numero y le decimos si es primo o no
RANGE: RANGe nos permite definir un rango entre los elementos de una coleccion(listas, diccionarios), es decir, 
'''

# funciones

def primos():

    numero = int(input('Introduce el numero y Averigua si tu numero es PRimo o no: '))

    if numero < 2:
        print('Estos numero no son primos')

        return False

    elif numero == 2:
        return True
    
    elif numero > 2 and numero % 2 == 0:
        return False
    else:
        # La "i" toma erl valor de los RANGE
        for i in range(3, numero):
            # Si "i" es divisible de "i" que en este caso lo hara con 3, i es gual a 0, hazme esto
            if numero % i == 0:
                return False
    return True

# def Inicio():

#     if 


# MAIN. Inicio para ejcutar el codigo

if __name__ == "__main__":
    # Al hacer un for con un rango de 1 a 100, que seran esa cantidad 10, y al poner la funcion(), repetira esa funcion 10 veces
    # Es decir al final es un bucle, el RANGE nos permite definir una cvantidad de veces que se repita
    for i in range(1, 10):
        primos()