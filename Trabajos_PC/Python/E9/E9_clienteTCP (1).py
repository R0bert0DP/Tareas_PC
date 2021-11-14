import argparse
import socket
from cryptography.fernet import Fernet

#creacion de argpase
des=""" Cliente TCP
    Modo de usar clienteTCP.py -msj "Mensaje a Enviar" """
parser = argparse.ArgumentParser(description='Port scanning', epilog=des,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('-msj', metavar='MSJ', dest="msj",
                    help='Mensaje que desea enviar',required=True)
args = parser.parse_args()
#Inicia el objeto de encriptación. 
key=Fernet.generate_key()
cifrar=Fernet(key)
#Guarda tu clave de encriptación en el archivo y Cierra el archivo.
file=open('clave.key','wb')
file.write(key)
file.close()
#mensaje en argparse -> bytes
mensaje = args.msj
mensajeBytes = mensaje.encode() 
#Muestra en pantalla el mensaje que se va a enviar. 
msj_cifrado = cifrar.encrypt(mensajeBytes)
print("Mensaje enviado: ",mensaje)

#Variables de ip y puerto
TCP_IP="127.0.0.1"
TCP_PORT=5005
BUFFER_SIZE=2048

#Enviar mensaje encriptado
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP,TCP_PORT))
sock.sendall(msj_cifrado)
#Recibir el mensaje
respuesta=sock.recv(BUFFER_SIZE).decode()
sock.close()
print("Respuesta recibida: ",respuesta)
