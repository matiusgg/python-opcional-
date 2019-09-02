
# def paises():


#     print('BIENVENIDO A TU SITIO PARA CONVERTIR NUMEROS EN UN NUMERO AUTOMATICO')
#     print('El numero debe ser de 9 digitos CRACK')



    # numero = input('Introduzca el numero que quiere:')

def numeroBonito():

    print('BIENVENIDO A TU SITIO PARA CONVERTIR NUMEROS EN UN NUMERO AUTOMATICO')
    print('El numero debe ser de 9 digitos CRACK')



    numero = input('Introduzca el numero que quiere:')

    print(len(numero))

    if len(numero) == 9:

        print('[fr].FR(+33)')
        print('[pt].POR(+351)')
        print('[hol].HOL(+31)')
        print('[col].COL(+54)')

        pais = input('Introduzca el pais que quiere formar su numero: ')

        paises = {
            'fr':33, 
            'pt':351,
            'hol':31,
            'col':54
            } 

        # numero.insert(0, f'(+{paises[pais]})')

        listaNumeros = []

        for i in numero:

            listaNumeros.append(i)

        print(listaNumeros)

        listaNumeros.insert(0, f'(+{paises[pais]})')
        listaNumeros.insert(4, ' - ')
        listaNumeros.insert(8, ' - ')
        

        numero_cadena = ''.join(listaNumeros)

        numero_conblanco = numero_cadena.replace(' - ', ' ')

        print(numero_cadena)

        print(numero_conblanco)

  

        # print(f'{listaNumeros[0]} {listaNumeros[1:4]} - {listaNumeros[4:7]} - {listaNumeros[7:10]}')
        # print(f'{listaNumeros[0]} {listaNumeros[1:4]}  {listaNumeros[4:7]}  {listaNumeros[7:10]}')                              
    
    
    else:
        print('Deben ser nueve digitos CRACK')



# COMO LO HIZO EL PROFE, MI FORMA ESTA BIEN TAMBIEN:

# como sabemos el string de por si es una lista de caractreres, Usamos el INSERT para introducir elementos en este caso,
# los elementos de un telefono

# numero.insert(0, f'(+{diccionario[input]')
# numero.insert(0, '(+34)')
# numero.insert(4, ' - ')
# numero.insert(8, ' - ')

# # Colocar los elementos con una sola fila, unir los elementos con un caracter de por medio

# numero_cadena = ''.join(numero)

# numero_conblanco = numero_cadena.replace('-', ' ')

# OTRA FORMA:

# lista = []

# for i in numero:

#     lista.append(i)



        






if __name__ == "__main__":
    numeroBonito()