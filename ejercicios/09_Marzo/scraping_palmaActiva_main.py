import requests

url = 'https://palmaactiva.palmademallorca.es/portal/PALMA/palmaactiva/contenedor1.jsp?seccion=buscador_acc.jsp&language=es&codResi=1&codMenu=2224'

palmaActiva = requests.get(url)

from bs4 import BeautifulSoup

soup = BeautifulSoup(palmaActiva.text, 'lxml')

#************************************************

def cursosLinks(etiquetaGeneral, etiqueta, valorAtributo, etiquetaEspecifica):

    lista_enlaces = []

    try:
    
        menuWeb = soup.find(etiquetaGeneral, attrs={etiqueta: valorAtributo}).find_all(etiquetaEspecifica)

        #* Colocar en un diccionario, el titulo del link como llave y el valor como el link
        # diccenlacesCursos = {link.get_text():link.get('href') for link in menuWeb}
        #* Pero tambien podemos meter directamente los links en una lista
        for link in menuWeb:

            lista_enlaces.append(link.get('href'))

        # return diccenlacesCursos
        return lista_enlaces
    
    except:
        print('No han encontrado enlaces')

print(cursosLinks('table', 'id', 'lista', 'a'))

links_cursos = cursosLinks('table', 'id', 'lista', 'a')


#************************************************


def albergacurso(url):

    #*diccionario cursos
    cursos_dicc = {}
    try:
        #* Vamos a recoger el html del articulo
        html = requests.get(url)
        #* Si el code que nos reporta esta acción es 200, entramos con BeautifulSoup
        if html.status_code == 200:
            curso = BeautifulSoup(html.text, 'lxml')
            #*Extraer titulo de la curso
            #* Buscamos en la página la etiqueta, para saber cual tipo es, así también con el resto de lo que queramos buscar
            titulo = curso.select('div.header h3.title')
            print(titulo.text)
            if titulo:
                cursos_dicc['titulo'] = titulo.text
                
            else:
                
                cursos_dicc['titulo'] = None

            return cursos_dicc
                
#             #* Extraer fecha de la curso
#             #IMPORTANTE: No es aconsejable imprimir con .text cosas como fechas, ya que la página lo tendrá de una manera
#             #* y como vamos a usar este dato, lo ideal es que lo convirtamos en forma anglosajona estandar, usando get('datetime/tipoEtiqueta')
#             fecha = curso.find('time', attrs={'itemprop':'datePublished'}).get('datetime')
#             print(fecha)
            
#             if fecha:
#                 cursos_dicc['fecha'] = fecha
                
#             else:
                
#                 cursos_dicc['fecha'] = None
                
#             #* Para extraer el <img> de una imagen, en este caso buscando con el inspector de elementos, el tipo de etiqueta, y sus atributos.
#             media = curso.find('figure', attrs={'id': 'fotografia_wrapper'}).find_all('img')
            
#             if len(media) == 0:
#                 print('No hay imagenes')
    
#             else:
#                 #* Coger el ultimo elemento, para ello usamos [-1], porque la última?, porque comúnmente la última es la más importante de las demás.
#                 imagen = media[-1]
#                 #* de la imagen, sacamos el SRC, donde se extrae la imagen.
#                 img_src = imagen.get('src')
#                 print(img_src)
                
#                 img_correcto = requests.get(img_src)
                
#                 cursos_dicc['imagen'] = img_correcto.content
                
#             #* Lista con el contenido de la curso
#             lista_contenido_curso = []
                
#             #* contenidocurso
#             contenidocurso = curso.find('div', attrs={'itemprop':'articleBody'}).find_all('p')
            
# #             print(contenidocurso)
            
#             for contenido in contenidocurso:
                
#                 lista_contenido_curso.append(contenido.text)
                
# #             print(lista_contenido_curso)

#             #* JOIN para jugar los contenidos de la curso
#             juntarContenidos = ' '.join(lista_contenido_curso)
            
#             print(juntarContenidos)
            
#             #* Agregar juntarContenidos en el diccionario de la curso.
#             cursos_dicc['contenidocurso'] = juntarContenidos
                
#         return cursos_dicc
    
#     #* Cuando encuentres una excepción, independientemente del tipo de excepción, recogela.
    except Exception as error:
        print('ERROR')
        print(error)
        print('\n')

print(albergacurso(links_cursos[0]))


#*****************************************************+***

#* Ahora haremos un bucle, para sacar toda la información de los cursos, a partir de un bucle con los links de los cursos

# for linkCurso in links_cursos:

#     albergacurso(linkCurso)

#* TERMINAR ESTE EJERCICIO