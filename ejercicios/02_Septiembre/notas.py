



def run():

    print('''
    BIENVENIDO A TU PLATAFORMA PROFESOR:
    NUESTRO SISTEMA LE AYUDARA A SABER QUIEN APROBO Y QUIEN NO

    
    Escoge tu alumno:

    1. Mateo
    2. Jaume
    3. Jose
    4. Lolo
    5. julia
    6. Jorge
    7. Cristian
    8. Adrian
    9. Petro
    10. Fran
    11. Alejandro
    12. Luis
    13. Jordi
    14. Alexis
    15. David

    ''')

    # listaAlumnos = {
    # 'Mateo' = [],
    # 'Jaume': [],
    # 'Jose': [],
    # 'Lolo': [],
    # 'Julia': [],
    # 'Jorge': [],
    # 'Cristian': [],
    # 'Adrian': [],
    # 'Petro': [],
    # 'Fran': [],
    # 'Alejandro': [],
    # 'Luis': [],
    # 'Jordi': [],
    # 'Alexis': [],
    # 'David': []}

    # aprobados = []

    # suspendidos = []

    # TIENES QUE DEFINIR LAS COLECCIONES FUERA DE LOS BUCLES, SI QUIERES QUE CON EL BUCLE TE VAYA AGREGARNDO 
    # POR CADA VUELTA UN NUEVO VALOR, YA QUE SI LO DEFINES DENTRO DEL BUCLE, LO QUEHARAS ES QUE SOLO SE CREARA ESA COLECCION
    # CUANDO EL BUCLE SE EJECUTE POR LO CUAL CUANDO TERMINE EL BUCLE, NO NOS APARECERA COMO QUERAMOS PORQUE NO TENEMOS ESA COLECCION FUERA
# PARA SEGUIR JUGANDO CON EL SINO QUE UNICAMENTE SE CREA EN EL BUCLE.


    notas = {}

    aprobados = {}

    suspendidos = {}

    for i in range(1):

        alumno = input('Introduce el alumno que quieres calificar: ')


        control1 = float(input('Introduce la nota del control1: '))
        control2 = float(input('Introduce la nota del control2: '))
        control3 = float(input('Introduce la nota del control3: '))

        mediaControles = ((control1 * 0.1) + (control2 * 0.1) + (control3 * 0.1))

        print( mediaControles)

        final = float(input('Introduce la nota del final: '))

        mediaFinal = final * 0.7

        total = mediaControles + mediaFinal

        print(total)

        notas[alumno] = [control1, control2, control3, final, total]
    
 

        if total >= 5:

            print(f'Haz aprobado es superior a 5, tu nota es {total:.2}')


            # aprobados.append(alumno)

            aprobados[alumno] = total

            # print(aprobados)

            
    
        else:

            print(f'No haz aprobado tu nota es emnor a 5, tu nota es: {total:.2}')

            # suspendidos.append(alumno)

            suspendidos[alumno] = total

            # print(suspendidos)

    print(aprobados)
    print(suspendidos)
    print(notas)

    pregunta = int(input('Escoge la opcion: 1.Aprobados, 2.Suspendidos, 3.Notas Estudiantes: '))

    if pregunta == 1:

        print(aprobados.values())

    elif pregunta == 2:

        print(suspendidos.values())

    elif pregunta == 3:

        print(notas.items())

    else:

        print('No has escogido ninguna opcion')
    

    # COMO LO HIZO EL PROFESOR

    # notas = {}

    # aprobados = {}

    # suspendidos = {}

    # for i in range(3):

    #     alumno = input('Introduce el alumno que quieres calificar: ')


    #     control1 = float(input('Introduce la nota del control1: '))
    #     control2 = float(input('Introduce la nota del control2: '))
    #     control3 = float(input('Introduce la nota del control3: '))


    #     final = float(input('Introduce la nota del final: '))


    #     notas[alumno] = [control1, control2, control3, final, total]

        valoresNotas = notas[alumno]

        controles = 0

        for i in range(3):

            controles += valoresNotas[i]

        
        controles = (controles/3) * 0.3

        final = (notas[3] * 0-7) + controles
    
 

    #     if final >= 5:

    #         print(f'Haz aprobado es superior a 5, tu nota es {final:.2}')


    #         # aprobados.append(alumno)

    #         aprobados[alumno] = final

    #         # print(aprobados)

            
    
    #     else:

    #         print(f'No haz aprobado tu nota es emnor a 5, tu nota es: {final:.2}')

    #         # suspendidos.append(alumno)

    #         suspendidos[alumno] = final

    #         # print(suspendidos)

    # print(aprobados)
    # print(suspendidos)
    # print(notas)









if __name__ == "__main__":
    run()