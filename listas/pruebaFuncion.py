# dfuncion compare dos numero cual mayor y cual e smenor o igual



# def comparar():

#     numero01 = float(input('Introduce el numero 1: '))
#     numero02 = float(input('Introduce el numero 2: '))

#     if numero01 > numero02:
#         print(f'numero01 = {numero01:.2f} es mayor a numero02 = {numero02:.2f}')
#     if numero01 < numero02:
#         print(f'numero02 = {numero02:.2f} es mayor a numero01 = {numero01:.2f}')
#     if numero01 == numero02:
#         print(f'numero01 = {numero01:.2f} es igual a numero02 = {numero02:.2f}')

# comparar()

# Si lo hicieramos con parametros

# numero01 = float(input('Introduce el numero 1: '))
# numero02 = float(input('Introduce el numero 2: '))

# def comparar2(numero01, numero02):


#     if numero01 > numero02:
#         print(f'numero01 = {numero01:.2f} es mayor a numero02 = {numero02:.2f}')
#     if numero01 < numero02:
#         print(f'numero02 = {numero02:.2f} es mayor a numero01 = {numero01:.2f}')
#     if numero01 == numero02:
#         print(f'numero01 = {numero01:.2f} es igual a numero02 = {numero02:.2f}')

# comparar2(numero01, numero02)

# comparar ahora pero con tred numeros

# def comparar2():
#     numero01 = float(input('Introduce el numero 1: '))
#     numero02 = float(input('Introduce el numero 2: '))
#     numero03 = float(input('Introduce el numero 3: '))

#     if numero01 > numero02 and numero01 > numero03:
#         print('\n', f'numero01 = {numero01:.2f} es mayor')
#         if numero02 > numero03:
#             print(f'numero02 = {numero02:.2f} es mayor que numero03 = {numero03:.2f}, por lo cual numero03 = {numero03:.2f} es el menor')
#         if numero03 > numero02:
#             print(f'numero03 = {numero03:.2f} es mayor que numero02 = {numero02:.2f}, por lo cual numero02 = {numero02:.2f} es el menor')
#         if numero02 == numero03 or numero03 == numero02:
#             print(f'numero02: {numero02:.2f} y numero03: {numero03:.2f} son iguales')
#     if numero02 > numero01 and numero02 > numero03:
#         print('\n', f'numero02 = {numero02:.2f} es mayor')
#         if numero01 > numero03:
#             print(f'numero01 = {numero01:.2f} es mayor que numero03 = {numero03:.2f}, por lo cual numero03 = {numero03:.2f} es el menor')
#         if numero03 > numero01:
#             print(f'numero03 = {numero03:.2f} es mayor que numero01 = {numero01:.2f}, por lo cual numero01 = {numero01:.2f} es el menor')
#         if numero01 == numero03 or numero03 == numero01:
#             print(f'numero01: {numero01:.2f} y numero03: {numero03:.2f} son iguales')
#     if numero03 > numero02 and numero03 > numero01:
#         print('\n', f'numero03 = {numero03:.2f} es mayor')
#         if numero02 > numero01:
#             print(f'numero02 = {numero02:.2f} es mayor que numero01 = {numero01:.2f}, por lo cual numero01 = {numero01:.2f} es el menor')
#         if numero01 > numero02:
#             print(f'numero01 = {numero01:.2f} es mayor que numero02 = {numero02:.2f}, por lo cual numero02 = {numero02:.2f} es el menor')
#         if numero02 == numero01 or numero01 == numero02:
#             print(f'numero01: {numero01:.2f} y numero02: {numero02:.2f} son iguales')
#     if numero01 == numero02 == numero03:
#         print(f'numero01: {numero01:.2f}, numero02: {numero02:.2f} y numero03: {numero03:.2f} son iguales')
# comparar2()

# comparar2() pero sin tantos if's

# COMO LO HIZO EL RPOFESOR:

def comparar2():

    numero01 = float(input('Introduce el numero 1: '))
    numero02 = float(input('Introduce el numero 2: '))
    numero03 = float(input('Introduce el numero 3: '))

    

    lista = [numero01, numero02, numero03]
        lista.sort(reverse=True)

        print(f'Numero mayor: {lista[0]}')

        lista.reverse()

        print(f'Numero mas bajo: {lista[0]}')

        print(f'Numero intermedio: {lista[1]}')
      
          





        

            
       
    


comparar2()

# Sacar letra DNI ahora en python

def letraDNI(dni):
    
    listaLetra = 'TRWAGMYFPDXBNJZSQVHLCKEO'

    letra = listaLetra[dni%23]

    print(f'{dni}{letra}'.upper())


letraDNI(57865699)

