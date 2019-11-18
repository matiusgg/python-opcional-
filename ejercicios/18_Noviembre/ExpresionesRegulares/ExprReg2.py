import re

frase = 'hoy es lunes y me suenan las tripas el lunes de no poder comer paella'

#* Pero si la PALABRA se repite muchas veces dentro de un texto, usamos FINDALL que nos lo metera en una lista.
palabra = 'lunes'

print(re.findall(palabra, frase))
#* Y si queremos verlo contadamente, pues usamos COUNT/LEN(len seria lo ideal porque pues la lista tiene ya
#* en si cuantas veces se repite en el texto), ya que findall nos devuelve una lista.
print(len(re.findall(palabra, frase)))

#* Es preciso saber que obviamente en PALABRA pongamos los caracteres precisos como estarian en el texto.
