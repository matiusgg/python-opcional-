"""
Supongamos que tenemos un BD de datos y queremos sacar las direcciones que sean de palma mediante el
codigo postal, por lo cual usaremos las EXPRESIONES REGULARES para solucionar estas busquedas.
Porque usar las expresiones regulares y no el propio sELECT de SQL, porque si tenemos que hacer la busqueda,
en una BD que no separe el Codigo Postal ni la ciudad ni la direccion sino que ponga todo de golpe, en un solo atributo
nos dificultaria mucho la busqueda. Por lo cual usamos las ER.
ejercicio: Tenemos 5 calles de palma con su codigo postal de que tiene palma, del 07001-07015. La cuestion es que
estas direcciones no siempre mantienen un orden a la hora de poner le codigo postal-ciudad-calle, si no que puede
ser escrito de mil maneras, por lo cual las ER nos permiten que sin importar el orden en el que este el Texto, en este caso
la dirección podamos hacer la busqueda sin problemas. La busqueda tiene que ser mediante el codigo postal.
"""

import re

listaCalles = [
    'Avenida Argentina 189 07001 Palma de Mallorca',
    'Palma de Mallorca 07003 Avenida Joan March',
    '07002 Palma de Mallorca Calle Jacint Verdaguer',
    '07004 Calle Eusebi Estada Palma de Mallorca',
    'Avenida Alexandre Rossello'
]

for cp in listaCalles:

    #* IMPORTANTE: A diferencia de FINDALL, SEARCH y MATCH nos viene bien para buscar patrones en texto como en este caso,
    #* pero SEARCH es mejor si quiere gastar menos recursos.
    #* [0-1]: Es el caracter que ira entre 0-1, y el siguiente caracter de [0-5]. Por lo cual solo puede llegar hasta 15.
    if re.search('070[0-1][0-5]', cp, re.IGNORECASE):

        print(cp)

#* --------------------------------------------------------

#* IMPORTANTE: OBVIAMENTE NO METER UN TOCHO DE CONTENIDO DE TEXTO DE UN LIBRO POR EJEMPLO EN UNA VARIABLE
#* ESO NO ES VIABLE, PONLO EN UN JSON O BASE DE DATOS. PARA NO SOBRECARGAS EL ARCHIVO. PERO EN ESTE EJERCICIO VAMOS
#* A COLOCARLO EN UNA VARIABLE, VSC TE DERJA DE RECONOCER EL STRING SI EL STRING ES MUY LARGO COMO UN AVISO DE QUE HACER ESO
#* NO ES VIABLE.

libro = '\cx3 Todo mundo conoce a una "chica buena". Es la mujer que compensa de más, que le da todo a un hombre que apenas conoce , sin que él tenga que invertir mucho en la relación. Es la mujer que se entrega ciegamente porque desea con demasiado ahínco ser correspondida. Es la mujer que hace lo que cree que a su hombre le gustaría o querría porque quiere mantener la relación a cualquier costo. Toda mujer ha hecho esto en algún momento. Es verdad que la revista de modas promedio le da a la mujer ridículos consejos para las relaciones, que hacen más fácil entender por qué las mujeres están deseosas de compensar de más: "Hazte la difícil y después cocínale una cena de cuatro tiempos. . . hornea galletas en forma de corazón con coberturas exóticas importadas de Malasia ( como las de Martha Stewart).* Que no se te olviden los pequeños mantelitos de papel picado y las fresas orgánicas por las que manejaste durante dos horas. Después sírveselo todo en la segunda cita, vestida con un pequeño camisón negro de encaje". ¿Para qué sirve esta receta? Para un desastre. Especia lmente en lo concerniente a tratar con un hombre. Con u na advertencia: si lo persigues vestida con un amis ón negro, primero tendrá sexo contigo ... y después va a huir. ¿por qué los hombres huyen d e situaciones como ésta? orr en porque la manera de actuar de la mujer no sugiere que ella se dé un valor alto a sí misma. La relación es nueva, y el lazo entre ellos está relativamente vacío; pero ella ya . ., . Jugo su meJor carta. E l hecho de que ella esté deseosa de compensar de más a un virtual extraño sugiere de inmediato una de dos cosas. Él va a asumir que ella está desesperada, o va a asumir que ella q u iere acostarse con todos los hombres desde el primer momento. O ambas opciones. Lo que se pierde en el camino es que él aprecie todo el esfuerzo que ella hizo. Una vez que un hombre comienza a perder el resp e to por una mujer porque ella acepta devaluarse sutilmente, también va a perder el d eseo de acercarse a ella. Con o sin camisón. Por otra parte , una chica de ensueño no se mata por impresionar a nadie. Por esto, la mujer de la que él se enamora d e verdad no tiene que servir una cena de cuatro tiempos. Y t ampoco la verás sacando su vajilla buena. Empezará cocinándole una cena de un solo tiempo. (Palomitas de n1aíz.) Sin mantelitos de papel picado. Cualquier recipiente de plástico sirve. Sencillamente le preguntará a su invitado: "¿Qué prefieres, la bolsa o el recipiente?" Seis meses después cocina algo y le sirve un plato de comida caliente. ¿y qué piensa él? "i Qué bien! i Soy especial!" No importa si es pasta con salsa comercial servida con ,, albóndigas que compraste en el Deli de la esquina. El c;lirá: "iEsta es la mejor pasta que he comido en mi vida!". Ahora se siente como un rey. Y la única diferencia es la cantidad de tiempo y esfuerzo que tuvo que invertir al principio. No obtuvo todo desde el primer momento, y así lo aprecia más. Esto no trata sobre cómo jugar un juego o cómo mantpular a otra persona. Trata sobre si realmente te ves necesitada, o si puedes mostrarle, genuinamente, que eres su igual dentro de la relación. Trata sobre tu capacidad para ser independiente dentro de la relación. ¿Qué pasaría si desde el primer día estás. dispuesta a complacerlo en todo? Él pensaría que estás desesperada, y querría ver hasta dónde estás dispuesta a llegar. Es parte de la naturaleza humana. Comenzaría a probarte desde el primer momento. Mientras más maleable te volvieras, más {a que lo complacieras. Instantáneamente te vería una pila Duracell, en eso de "¿Hasta dónde llegará? to podré obtener de ella?". chicas buenas deben saber lo que la cabrona comde. Dar demasiado, o estar demasiado dispuesta a placer, disminuye el respeto de un hombre; da el beso muerte a su atracción y pone un límite de tiempo a la ión. La mayoría de los hombres no ven a una mujer que está puesta a hacer todo lo que se le pide como alguien que ce un desafío mental. Las mujeres inteligentes cometen rror de asumir que por tener un título de educación super, porque pueden mantenerse firmes en un debate polío y porque entienden sobre fondos de inversión, le pueden frecer estimulación mental a un hombre durante la cena. ro el desafío mental tiene poco que ver con la conver- . , CIOn. (Damos por descontado que si ella cree que Al Green y Alan Greenspan son la misma persona, entonces ... Torre de control, tenemos un problema.)* Por lo general, el desafío mental tiene que ver con si tú esperas que te respeten. También tiene que ver con la forma n la que te relacionas con él. Tiene que ver con que él sepa que tú no tienes miedo a estar sin él. La chica buena comete el error de estar disponible todo 1 tiempo. "No quiero juegos", dice. Así que le deja ver lo asustada que está de no tenerlo y él pronto siente que tiene un , control total sobre ella. Este suele ser el punto en el que las , mujeres empiezan a quejarse diciendo: "El nunca tiene tiempo para mí. No es tan romántico como antes". La cabrona es más selectiva sobre su disponibilidad. Está disponible algunas veces; otras no. Pero es amable. Quiero decir lo suficientemente amable para considerar las preferencias de él sobre cuándo verla para poder, algunas veces, complacerlo. ¿Traducción? Él no tiene un control absoluto sobre ella. ¿Qué pasa con la mujer que deja todo para ir a ver a un hombre? Ese hombre también sabe que tiene un control absoluto sobre ella. Después de un par de citas, sale una noche con sus amigos, regresa a medianoche, la llama, y ella sale corriendo a verlo. Cuando una mujer va a ver a un hombre en la madrugada, lo único que le hace falta es un letrero de neón en el techo de su coche que diga: ENTREGAMOS A DOMICILIO. Tu tiempo con él debe ser significativo. U na semana después de que conoce a un hombre, la chica buena se sienta en una silla, aburridísima mientras él hace algo que le interesa. Tal vez esté viendo deportes por televisión, limpiando su equipo de pesca, tocando la guitarra o trabajando en su coche. Ella está descontenta pero no hace ningún comentario. En lugar de eso, trata de pasarlo lo mejor ible y mata el tiempo de una manera cortés, con tal de r con él. Por otra parte, la cabrona hace los comentarios sufintes. De hecho se queja todo el tiempo. Quejarse no es lo, porque así él sabe que no puede pasar por encima de lla. Pero recuerda, el desafío mental no tiene nada que ver n ser verbalmente combativa. Tiene que ver con tus aciones y con cuánto de ti misma estás dispuesta a ceder. Por jemplo, él dice que le gustan las rubias. Tú eres de piel scura, ojos oscuros y cabello negro. La próxima vez que te ve, ya te lo decoloraste y teñiste tus cejas para que combinaran. ¿Traducción? Sentirá que tiene el control absoluto obre ti.  Al hombre el amor le nace por el estómago", suelen decir. Es verdad, pero nadie dijo que debes esclavizarte durante seis horas para alimentarlo. Ya sea que coma fuera o que ordenes comida para llevar, el estómago se llena, y sigue habiendo el amor suficiente. Principio útil: si está caliente, se lo va a comer. El resto es esfuerzo desperdiciado . Las mujeres están condicionadas para entregarse por completo. Todavía no he visto en ninguna revista para hombres un artículo que explique cómo cocinar una cena de cuatro tiempos para una mujer. Lo más cerca que pueden llegar a una receta es la sección para fi~icoculturistas, en la que enseñan a los chicos a mezclar unas cuantas claras de huevo con germen de trigo. Toco el tema de la cocina porque es una de las muchas formas en que las mujeres dan demasiado. No quiero decir que te olvides completamente de cocinar. Tal vez es su aniversario y ya llevan juntos todo un año. Tal vez es su cumpleaños y quieres hacer algo especial por él. Cocinar para él en alguna ocasión especial, y después de que se lo haya ganado, es un "regalo" bonito. Pero no es un regalo si se lo das desde un principio. Y como éste es un libro para mujeres, sería negligente de mi parte no incluir algunas recetas para esas primeras semanas de relación. Y, a diferencia de las recetas de Martha Stewart, las siguientes son fáciles de recordar. Ni siquiera necesitas un libro para guardarlas. Recomiendo las palomitas por su conveniencia y por la rapidez en su preparación. Primero pon la bolsa dentro del horno de microondas. Cuando todos los granos hayan reventado, saca las palomitas del horno con cuidado, porque van a estar muy calientes. Asegúrate de utilizar un guante para cosas calientes, un del~ntal y una espátula para ayudarte con la remoción de las palomitas del horno. Esto no sólo dejará impresionado a tu invitado, sino que también te hará ver como alguien que sabe lo que está haciendo. Si te das cuenta de que las palomitas se quemaron, fijate qué parte es la que se quemó. Si la parte superior de la bolsa se puso negra, tira las palomitas que están oscuras y salva el resto colocándolas en un recipiente. Sirve las palomitas amarillas a tu invitado y ajusta el tiempo del horno para hacer .,,. una bolsa nueva para ti. Raciones: una y media (suficiente). gua al fuego hasta que hierva y sumerge dos salchichas . Cocínalas durante cinco minutos hasta que se endurezcan n ligeramente a/ dente. Sirve a tu invitado una bebida ante (Koo/-Aid) y envíalo al balcón para que pueda lar la vista; recuerda que la ambientación lo es todo. do no te esté viendo corta las salchichas en rebanadas y un palillo de dientes a cada una de ellas. Como Martha ert, puedes expresar tu creatividad con una gran variedad palillos de diferentes colores. Ahora, sirve las pequeñas hlchas con dos "delicadas salsas" dispuestas una junto a la : cátsup y mostaza. Y nunca te refieras a esto como readas de salchicha, siempre llámalas "Delicias salseadas Ahora el postre: una rebanada de pastel ( comercial) rvida con café (instantáneo), y unas mentitas siempre le n un toque sofisticado a la cena. Te recomiendo los sabores nta, hierbabuena o Trident. Sabrás que la cena fue un éxito cuando él insista en vitarte a cenar fuera la próxima vez. Nunca más lo oirás ir: "Oye, ¿qué hay para cenar?". Si después de algún tiempo, alguna vez mete la pata y te de que cocines para él, sólo tienes que ofrecerte a cocinar spccialidad: palomitas de maíz, salchichas y un pastel crcial, servidos con café y Kool-Aid para acompañarlos. después comienza a arreglarte porque antes de una hor~ ya habrá reservado en un restaurante. La cabrona no es la mujer que se queda en casa y trabaja horas extra refinando sus técnicas para "atrapar hombres". Sólo siente que todo lo que debe hacer al principio es enfocarse en ser una buena compañía. Y esto es más que suficiente hasta que él se gane la "silla de capitán" d.el yate. Al principio, pon especial atención y toma nota de lo siguiente: si él no está dispuesto a mover un dedo durante el cortejo, te está dejando ver desde ese momento que no tiene nada que ofrecer en un futuro. Esta conducta no tiene nada que ver con tu valía. Tiene todo que ver con lo que él tiene para ofrecer. Y también tiene que ver con la forma en la que tú te presentas. ¿Estás trabajando horas extra? Si él tiene mucho que ofrecer pero tú no le permites ofrecértelo , no tendrá más opción que retroceder. Cuando una chica bu ena da demasiado, su conducta dice: "Lo qu e tengo para ofrecer no es suficiente, y lo que yo soy no es suficiente" . Al contrario , la cabrona da un mensaje diferente : "Lo que soy es suficiente. Tómalo o déjalo". Y ahora, una comparación: Las bases se establecen desde el primer día. Desde el rincipio, él conscientemente ( sí, conscientemente) trata de ntcnder los parámetros y de saber hasta qué punto se puede lir con la suya. La etiqueta telefónica también dice mucho. ¿Esperas a uc él te llame antes de hacer planes? ¿Te descompones si él o te llama, se reporta o no llega como quedó? Si es así, no le estás dando una lección sobre puntualidad. que estás haciendo es demostrarle que tiene un control bsoluto sobre ti, y éste no es un buen men ·saje para alguien uc acabas de conocer. Es un hecho que la mayoría de los hombres deliberamente no llaman, sólo para ver cómo respondes. Cuando na rnujer está m?lesta, es fácil saber cómo es. Yun hombre uedc medir, de una forma sencilla, cuánta falta le hace o Es parte de la naturaleza masculina probar las aguas para ver hasta dónde se pueden salir con la suya. Lo ves en la conducta de los niños y hasta en la de las mascotas. Así es como son. Retirarse es también algo que los hombres necesitan para reafirmarse. Ningún hombre te va a decir: "Querida, necesito reafirmación sobre mi relación contigo". En lugar de ello, se va a retirar para ver cómo...'

print(libro)
#* 1.limpiarlo de tildes
#* 2. Contador de palabras, sin ExpresionRegulares y con ExpresionesRegulares

#* LIMPIEZA
from unicodedata import normalize

enye = libro.replace('ñ', '#').replace('Ñ', '$')
frase = normalize('NFKD', enye)\
    .encode('ascii', 'ignore')\
        .decode('ascii')\
            .replace('#', 'ñ')\
            .replace('$', 'Ñ')

# print(frase)

#* CONTADOR

#* con ER:
#* Ponemos ' ', ya que cuando hay un espacio hay una palabra.
print(len(re.findall(' ', frase)))


#* sin ER:
print('Cantidad de palabras: ' + str(len(frase.split())))

#* Comprobar cuantas frases hay.

print(len(frase.split('.')))
print(len(re.findall('.', frase)))

#* Cuantas palabras se deberian acentuar/ cuantas se deberían acentuar y donde están.
#* Usaremos la misma variable, en donde originalmente tenemos las palabras bien acentuadas, con ningun error.
#* Por lo que DESPUES DE LIMPIAR, en donde ya no tendriamos ningun acento, averiguemos cuantas palabras se deberían acentuar del texto las cuales ya sabemos porque el texto originalmente ya los tenía antes de la limpieza, por lo cual
#* lo que queremos es CUANTAS.

acentos = ['á', 'Á', 'é', 'É', 'í', 'Í', 'ó', 'Ó', 'ú', 'Ú']

palabrasConAcento = []
mismaPalabraSinAcento = []
for i in acentos:

    for palabra in libro.split():

        if i in palabra:

            palabrasConAcento.append(palabra)

            palabraSinAcento = normalize('NFKD', palabra)\
                .encode('ascii', 'ignore')\
                    .decode('ascii')\
                        .replace('#', 'ñ')\
                        .replace('$', 'Ñ')

            mismaPalabraSinAcento.append(palabraSinAcento)

print('Total palabras que deberían tener acento: ' + str(len(palabrasConAcento)))

print('Misma palabra que antes tenian acento pero ahora no por el NORMALIZE: ' + str(len(mismaPalabraSinAcento)))

#* SIN LIMPIAR: Cuantas palabras hay mal acentuadas:

# for palabra in frase.split():

#     if 




