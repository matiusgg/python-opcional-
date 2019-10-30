'''
FUNCIONES LAMBDA: Es una funcion anonima y que se utiliza en Python para abreviar, resumir una funcion normal a la
minima expresión.
Serian las funciones de tamaño pequeño las que nos podriamos llevar/convertir a una funcion Lambda.
No necesariamente una funcion LAMBDA no necesita un nombre de variable ya que es anonima, por lo cual nos facilita
mucho.
'''

#* Ejemplo

#*Funcion standard
def primer_Triangulo(base,altura):

    return (base * altura) / 2

#* Funcion Lambda. Como vemos se pone nombreLambda = lambda parametros: expresion
Triangulo = lambda base, altura: (base * altura) / 2

print(Triangulo(4,4))

#*******************************

elevado_al_cubo = lambda numero: numero**3

print(elevado_al_cubo(2))

#*******************************

valor = lambda comision: f"!{comision}¡"

comisionUsuario = 1500

print(valor(comisionUsuario))

#*******************************

def imprimir(par):

    print(par)

#* Una LAMBDA que en su contendio llama a otra funcion, como vemos no necesariamente tenemos que poner
#* parametros en el LAMBDA.
command = lambda: imprimir('Hola')

#**********************************

#*Una funcion lambda llama a otra funcion lambda
llamada = lambda : command
