import smtplib, ssl 
import getpass

from email import encoders
from email.mime.base import MIMEBase  #envia contenido en bruto 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Datos para el imicio de sesion
username = input("Ingrese su usuario: ")
passw = getpass.getpass("Contraseña: ")

destino = input("Ingrese el destinatario: ")
asunto = input("Asunto: ")

#crear mensaje 
mensaje = MIMEMultipart("alternative")
mensaje["subject"] = asunto
mensaje["From"] = username 
mensaje["To"] = destino

html = f"""
<html>
<body>
    <p>Hola {destino}<br>
    Imagen de la tarea E14 
    Luis Roberto Diaz Pineda
    bonito fin profesora :D
</body>
</html>
"""
parte_html = MIMEText(html, "html")
#agregar el contenido al mensaje 
mensaje.attach(parte_html)

archivo = "meme_pc.jpg"

with open(archivo, "rb") as adjunto:  #rb=leer como bytes
    contenido_adjunto = MIMEBase("application", "octet-stream")  
    contenido_adjunto.set_payload(adjunto.read())

encoders.encode_base64(contenido_adjunto)

contenido_adjunto.add_header(
    "Content-Disposition",
    f"attachment; filename= {archivo}",
)

mensaje.attach(contenido_adjunto)
text = mensaje.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(username, passw)
    server.sendmail(username, destino, text)

