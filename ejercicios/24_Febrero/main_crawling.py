#
#* Libreria para navegar a travez de la web
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#* Abrir el navegador deseado
#* Variable con el driver que tiene distintos navegadores, recomendable Firefox()
driver = webdriver.Firefox()

#* Conectar a la url de restaurante
#* Al ejectuar nos abrirá el navegador, y nos aparecerá un icono de robotización en donde nos indica
driver.get('https://www.tripadvisor.es/Restaurants')

#* Pasos que vamos pedir que se hagan en la web para extraer información:

#*1. insertar palabra-clave en un input principal, ya sea de busqueda o uno de relevancia
#* buscamos su class en el html en el inspector de elementos
# input_restaurante = driver.find_element_by_class_name('nombreClassDelInput')
input_restaurante = driver.find_element_by_class_name('typeahead_input')

#* Limpiamos el input pra evitar inconvenientes
input_restaurante.clear()

#* Enviarle información(escribir en el input) al input desde python
input_restaurante.send_keys('Palma de Mallorca')

#* Ahora vamos a hacer que mediante RETURN de Keys, nos pulse el boton del input de enviar.
input_restaurante.send_keys(Keys.RETURN)

#* recoger informacion de la página 01 de restaurantes
import request
#*Parsear el código de html como lo haciamos con scraping
from bs4 import BeautifulSoup
import lxml

restaurantes = []
finalizar = 0

while finalizar < 3:

    #* Le vamos a dar tiempo de carga
    #* de 5 segundo de espera hasta que nos muestre la web, porque? para que el proceso de abrir el navegador
    #* pueda hacerce, ya que el código va más rapido. 
    import time
    time.sleep(5)
    #?SCRAPING, recogemos la información de la página
    #* Ahora a diferencia de main_scraping.py, usarmos current_url para que nos coja la url del navegador que hemos abierto con Crawling
    url = driver.current_url
    peticion = request.get(url)
    text_devolucion = peticion.text
    soup = BeautifulSoup(text_devolucion,'lxml')
    #* filtrar el contenido:
    #* titulos de los restaurantes
    restaurantes_lista = [[i.get_text(strip=True) for i in soup.find_all(class_="poiTitle")]]
    #* Agregamos esta lista a la lista restaurantes, ya que "restaurante tendrá toda la información  de las páginas las páginas."
    restaurantes.append(restaurantes_lista)

    #? CRAWLING
    #* ahora queremos hacer mediante el crawling que nos vaya pulsando los botones de siguiente página de restaurantes, para despues
    #* en la siguiente vuelta haga el SCRAPING
    #* Recordemos que para acceder clase a clase, tiene que ser como en css, punto a punto
    boton_siguiente = driver.find_element_by_class_name('nav.nex.rndBtn.ui_button.primary.taLnk')

    boton_siguiente.click()

    finalizar += 1

#* como vemso la dinamica del bucle es que por cada vuelta, vaya haciendo el scraping de cada página, para despues aplciar el crawling del boton
#* para ir a la siguiente página, y en la siguiente vuelta del bucle vuelva hacer LO MISMO. ahora si nos ponemos a pensaar tenemos la información de todos
#* los restaurantes de una página, dentro de python en una lista, donde cada elemento de la lista "restaurante" son listas con la información de cada
#* página.

for i in range(finalizar):
    print(f'*****************************{i + 1}')
    
    for y in restaurantes[0]:

        print(y)

        #* ahora saquemos en varias listas con elementos que serían las páginas con los detalles: nombre, valoración, tipo Cocina, precio
        #* hacer el proceso como con el ejemplo anterior, el proceso sería el siguiente: medianre crawling nos vamos al sitio de busuqeda
        #* donde queremos recopilar toda la información, creamos la lista donde se almacenará, creamos el bucle que adentro tiene el scraping para coger la información
        #* de esa página y despues crawling para pasar a la siguiente.
        #* Esto usanod FLASK para imprimir en una ruta lo antes mencionado.
        #* Realizar ejercicio, pero no en la parte de ofertas sino abajo en el resutlado de la busqueda de tripadvisor.
