import request

url = 'https://www.tripadvisor.es/SmartDeals-g187462-Majorca_Balearic_Islands-Hotel-Deals.html'

peticion = request.get(url)

#* Convertir la petición del html en texto, par aimprmir
text_devolución = peticion.text

# print(text_devolución)

#* Parsear el código de frontend, es decir
#* importamos bs4 para el scraping
from bs4 import BeatifulSoup
#* importanr lxml
import lxml

#* Convertir a un objeto el código de frontend
#* el 'lxml' lo que nos permite es pasar todo el script de frontend al html
soup = BeatifulSoup(text_devolución,'lxml')

#* filtraremos el contenido de las etiquetas de html que nos interese:
#*titulo del primer restaurante que me enseñe la web, entonces nos vamos a la web con la página y nos vamos en el navegador
#* al inspector de elemento, y buscamos el titulo de un restaurante y vemos si está en una etiqueta con sección, si la esta entonces
restaurante = soup.find(class_="nombreClaseQuecontieneElTitulo").get_text(strip=True)
#* Imprimamos el titulo
print(restaurante)

#* Ahora si queremos todos los titulos de la página:
#* como vemos se lo enviamos como una lista con los [], y dentro de este podemos hacer un bucle para que nos vaya sacando los titulos
#* con la función find_all
restaurantes = [i.get_text(strip=True) for i in soup.find_all(class_="poiTitle")]

print('Todos los restaurantes' + str(restaurante))

