'''
---------------------------
FUNCIONES DE ORDEN SUPERIOR
---------------------------
lAS FUNCIONES DE PYTHON PUEDEN TOMAR funciones como parametros y devolver funciones como resultado, y una función
que hace ambas cosas se llama funcion de ORDEN SUPERIOR. Además ya sabemos que python es multiparadigma, por eso con estas funciones estamos programando
en lo que se llama "Programaicon Funcional" que es otro paradigma.

Una de las funciones de Orden Superior, que ya hemos visto es LAMBDA.
'''

#*****************************************************************************
'''
FUNCION FILTER: Devuelve una colección de elementos filtrados que cumplan una condición.
Es decir 
'''

# Ejercicio para entender FILTER: Función que me calcule los números pares y me devuelva un TRUE

def numPar(par):

    if (par % 2) == 0:

        return True

print(numPar(4))

#*Lista que ira en la funcion FILTER
listNumeros = [23, 24, 25, 26]

#* Funcion FILTER
#* En este caso tendremos dos parametros, 1. Sera la funcion que hemos hecho de numPar() y 2. Sera la listaNumeros
#*Lo que hara es mirar los numeros pares de la lista, ya que la funcion numPar() en su parametro introduce los elementos de la
#*lista y mira cual es PAR, lo que hace basicamente es sacar una coleccion con los resultados de la condicion que tiene la funcion
#* numPar() como vemos tener 2x1 ya que tenemos la funcion() y la lista de una vez en una funcion FILTER
filtro_par = filter(numPar, listNumeros)

#* Nos mostrara un codigo en pantalla que es del objeto para verlo usamos LIST ya que en FILTER introdujimos es un LIST
#* aunque podemos verlo con un FOR
#* recordar que dependiendo de la coleccion que introduzcamos, en el print tenemos que convertirlo ya sea LIST o TUPLE u otra.
print(list(filtro_par))

#* Ahora con un LAMBDA para tenerlo mas resumido

lambdaFilter = filter(lambda numPar: numPar % 2 == 0, listNumeros) 

print(list(lambdaFilter))

