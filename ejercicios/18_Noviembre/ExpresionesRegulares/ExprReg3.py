import re

frase = 'hoy es lunes y me suenan las tripas el lunes de no poder comer paella y quiero irme en camion. El sábado también'

#* Pero si la PALABRA se repite muchas veces dentro de un texto, usamos FINDALL que nos lo metera en una lista.
palabra = 'lunes'

#* Limpliar la frase de tildes, esto viene bien por el tema de que nos limpia las tildes
from unicodedata import normalize

#* En donde, ENCODE llamamos a ASCII y DECODE lo despliega dentro del texto.
#* Y NORMALIZE hace el trabajo de limpieza.
# frase = normalize('NFKD', frase).encode('ascii', 'ignore').decode('ascii')
#* El problema que vendria que es ademas de limpiarnos las tildes nos limpia otras letras de otros idiomas, que ya influyen
#* directamente en el texto, por ejemplo en español, se perderia la Ñ

#* Para evitarlo usariamos REPLACE y reemplazandolos con caracteres extraños:
enye = frase.replace('ñ', '#').replace('Ñ', '$')
#* Ahora normalizamos, pero luego tambien volvemos a reemplazar los caracteres extraños por las ñ en este caso.
#* y asi volvemos el texto normal sin que nos afecte el normalize
#* Podemos usar '\' para seguir escribiendo abajo y sin que sea una linea super larga de codigo.
frase = normalize('NFKD', enye)\
    .encode('ascii', 'ignore')\
        .decode('ascii')\
            .replace('#', 'ñ')\
            .replace('$', 'Ñ')

#* ES IMPORTANTE QUE ANTES DE USAR EL NORMALIZE, REEMPLACEMOS LOS CARACTERES DE UN IDIOMA PARA QUE NO HALLAN PROBLEMAS.
print(frase)

#* Otra forma ams rapida seria alamcenar en un string, todos los caracteres de otros idiomas
a,b = 'áéíóú', 'aeiou'
#* Lo que ahce es convertir todos los caracteres de A en los caracteres  de B, viene bien para los acentos.
transferencia = str.maketrans(a,b)
#* Esto seria como un NORMALIZE pero el problema, es que si no ponemos todos los caracteres de otros idiomas, no nos lo hara.
#* Esto viene bien usarlo en un caso especifico.
print(frase.translate(transferencia))

palabra = 'sabado'

#* no nos dara problemas con SABADO porque con el NOrMALIZE lo hemos limpiado, asi que podemos hacer la busqueda normal y corriente.

print(re.findall(palabra, frase))

