# si la comprA ES MAYOR DE 50 ERUOS SE HARA DFESCUENTO DEL 
# si es menor o igual de 30 euros, frase para incentivar 15% de descuento 
#si esta entre 0 y 20 euros, no hay descuento
#IVa: precio * 0.21

print('\t COMPRA EN NUESTRO SUPERMERCADO \n')

# pescado = 10
# queso = 15
# pavo = 25

# Aqui usamos el +=, para que vaya sumando todos los precios

producto1 = str(input('Introduce el producto que quieres comprar: '))
precio = float(input(f'Precio del {producto1}: '))
producto2 = str(input('Introduce el producto2 que quieres comprar: '))
precio += float(input(f'Precio del {producto2}: '))
producto3 = str(input('Introduce el producto3 que quieres comprar: '))
precio += float(input(f'Precio del {producto3}: '))
# iva = precio * 0.21
# precio += iva



if precio >= 50:
# o tambien poniendo (precio * 15) / 100 
    descuento50 = precio * 0.15
    precio -= descuento50
    iva = precio * 0.21
    precio += iva
    print(f'Tienes una compra superior/igual a 50 euros, tienes un descuento del 15%, es decir esta cantidad: {descuento50:.2f}')
    print(f'\n Su compra sera entonces: {precio:.2f}')
    print(f'incluye IVA: {iva:.2f}')

elif precio > 20 and precio <= 30:
    print(f'Tiene usted la posibilidad de optar por un gran descuento,'
    f'pero tiene que introducir su codigo postal: \n')

    elegir = input('yes(Y)/no(N): ').upper()

    if elegir == 'Y':
        cp = int(input('Introduzca su codigo postal: '))
        descuento30 = precio * 0.1
        precio -= descuento30
        iva = precio * 0.21
        precio += iva
        print(f'tienes un descuento del 10%, es decir esta cantidad: {descuento30:.2f}')
        print(f'\n Su compra sera entonces: {precio:.2f}')
        print(f'incluye IVA: {iva:.2f}')
    else:
        print('Usted se lo pierde')
    
elif precio < 20 and precio > 0:
    iva = precio * 0.21
    precio += iva
    print(f'Su compra total es: {precio:.2f}. No incluye descuento')
    print(f'incluye IVA: {iva:.2f}')


# Total precio

print(f'\t\nTotal precio de la comnpra: {precio:.2f}euros')



