"""
ENVIAR UN EMAIL CON PYTHON
-------------------------
Python contiene tres módulos de Email
SMTP: Estandar para enviar correos
IMAP: Recibimos correo. buscar
POP: buscar.

Python tiene 3: smtplib, imaplib y poplib.
Usaremos SMTPLIB, que nos ayudarña a enviar correo

NO COLOCAR EN UN NOMBRE DE ARCHIVO: email.py
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#* CORREO DE ENVÍO
#* Correo de acceso al servidor
MI_CORREO = 'ponerCorreoDePrueba@gmail.com'
#Password de acceso
PASSWORD= 'contraseñaDePrueba'

#* Configuración del servidor de correo
server = smtplib.SMTP(host='smtp.gmail.com', port=587) # Servidor y puerto
server_gmail.starttls() # conexión tls
server_gmail.login(MI_CORREO, PASSWORD) # Nos servirá para inicar session

#* Crear mensaje
msg = MIMEMultipart()
#* Hay dos tipos de mensaje, mensajes planos() y otro 
mensaje = 'Probando el envío por email del texto plano con Python'
html_mensaje = """ <h2> Probando el envío por email del texto plano con Python</h2>"""

print(mensaje)

#*********************************************
#* maquetación del correo electronico
#* Configurar parámetros del mensaje a enviar
#* FROM, quien lo envía
msg['From'] = MI_CORREO
#* To: A quien va a ir
#* si queremos enviarlo a varias personas, podemos hacer un diccionario con los correos de las personas
#* y colocarlo en este. O un diccionario con la información de una query de unos correos de una base de datos
#* en un bucle sería nombreDiccionario[i]
msg['To'] = "onlylearnenglish2017@gmail.com"
#* Contenido
msg['Subject'] = "Prueba Con Python"

#* Agregar textod el mensaje
#* MIMETEXT: Tipo de mensaje
#* ATTACH es el que se encarga de juntar el mensaje al body del correo
#* probar con 'html' o 'plain' si funciona.
msg.attach(MIMEText(mensaje, 'html'))

#* Enviar Correo
server_gmail.send_message(msg)
#* Es importante borrando para limpiar la cache del servidor
del msg
#* Fin alizar sessión del SMTP
server_gmail.quit()
#* Si sale bien, muestranos que ha salido bien
print("Mensaje enviado correctamente")

#* AHORA NECESITAMOS PERMITIR A GMAIL,y dar autorización de que una aplicaicón externa
#* Pueda enviar correos
#* Para ello nos vamos, administrar tu cuenta de google -> seguridad -> acceso de apps no seguras(solo lo activaremos como prueba, pero hayq ue dejarlo desactivado)

#**********************************************

#* En el caso, de que queramos enviar muchos correos mediante un bucle por ejemplo
#* El gmial u otra aplcación de correo, te bloquea el gmail por exceso.
#*  en el caso,de tener una Base de Datos con correo para enviarles un mensaje, entonces tenemos que hacerlo pausado
#* Ya que asñi evitamos de que gmail nos bloquee la cuenta.

#* Y también en el caso de usar Scraping, si queremos que mediante un email nos diga que como fue el proceso de scraping, también tenemos que pausar
#* Ya que es probable de que en python tengamos mucha información, y nos haga muchos correos de como fue el proceso, por lo cual necesitariamos tambien
# una pausado entre ellos.

"""
EJERCICIO: SCRAPING A VARIAS PA´GINAS DE EMPRESAS DE FORMACIÓN CON CURSOS DE SOIB(palmaactiva, Ibecon, Edib): DONDE SACAREMOS
INFORMACIÓN COMO: titulo de curso, imagen del curso(si la hay), descripción, requisitos, fecha inicio y fin. 
Tenemos que filtrar por fechas para el tema de duplicados, porque pueden haber cursos del mismo nombre pero con diferentes fechas
yA CON LA INFORMACIÓN NOS LEVAREMOS ESTA INFORMACIÓN A LA ABSE DE DATOS
ESTA INFORMACIÓN NO DEBE DUPLICADA.
"""

El archivo miercolesUltimHora.ipynb, es un archivo tipo jupyter, VSC nos permite procesar archivos jupyter
y poder trabajar 