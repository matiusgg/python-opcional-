def pruebaEmail(mail):

    """
    Esta funcion prueba si tu email es valido. Si tiene un @ en su lugar, esta perfecto.
    Si el @ esta al principio o al final esta mal.
    Si no hay @, esta mal.

    Pruebas:
    >>> pruebaEmail('pepe@gmail.com')
    True
    >>> pruebaEmail('pepegmail.com')
    False
    >>> pruebaEmail('@pepegmail.com')
    False
    >>> pruebaEmail('pepegmail.com@')
    False
    """
    
    if '@' in mail and mail[0] != '@' and mail[::-1][0] != '@':
        return 'Correcto'

    else:
        return False

    #*COmo lo hizo toni
    # mail_usuario = mail.count('@')

    # if mail_usuario != 1 or mail.rfind('@') == len(mail)-1 or mail.find('@') == 0:

    #     return False

    # else:

    #     return True
    
print(pruebaEmail('hola@gmail.com'))

#* Importamos DOCTEST
import doctest
doctest.testmod()

        





print(pruebaEmail('holagmail.com'))