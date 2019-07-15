# CAJERO AUTOMATICO

# ingresar, retirar, mostrar y salir

saldo = 4000

opciones = float(input('Escoga la opcion: 1.ingresar, 2.retirar, 3.mostrar y 4.salir: '))

if opciones == 1:

    ingresar = float(input(f'Ingrese la cantidad: '))

    if ingresar != 0:
        ingreso = saldo + ingresar
        print(f'Ingresaste la cantidad de: {ingresar:.2f}€, El saldo actual es: {ingreso:.2f}€')

       
elif opciones == 2:

    retirar = float(input(f'Dinero a retirar: '))

    if retirar > saldo:
        print('No tienes suficiente dinero en la cuenta')
    else:
        retiro = saldo - retirar
        print(f'Has retirado la cantidad de {retirar:.2f}€, su saldo actual es {retiro:.2f}€ ')

elif opciones == 3:

    print(f'Tu saldo es el siguiente: {saldo:.2f}€')
elif opciones == 4:

    salir = float(input(f'Desear salir? 1.salir 2.no: '))

    if salir == 1:
        print('Has salido del cajero Automatico')
    else:
        print('No has salido del cajero Automatico')

        # Como lo hizo el profesor, es mas optimo:

        # if opcion == 1:
        #     extra = float(input('Cuanto dinero quiere ingresar: '))
        #     saldo += extra
        #     print(f'Dinero en la cuenta {saldo:-2f}euros')


