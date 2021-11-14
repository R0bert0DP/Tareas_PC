import socket
from cryptography.fernet import Fernet

TCP_IP="127.0.0.1"
TCP_PORT=5005
BUFFER_SIZE=2048
#objeto socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#bind se usa para convertir un socket en servidor
sock.bind((TCP_IP,TCP_PORT))
#Para que escuche las conexciones entrantes
sock.listen()
#Para que empiece a aceptar las conexiones entrantes
while True:
    print("Esperando una conexion")
    clientSocket, client_address=sock.accept()
    #Manejar una solicitud del clientes 
    try:
        print("Conexion desde",client_address)
        data=clientSocket.recv(BUFFER_SIZE)
        if data:
            #obtener la key del archivo  
            file=open("clave.key","rb")
            clave=file.read()
            file.close()
            cipher_suite=Fernet(clave)
            msjB=cipher_suite.decrypt(data)
            msj=msjB.decode()
            print("Mensaje recibido: ",msj)
            print("Enviando datos de vuelta al cliente")
            date=bytes("Enterado, bye!".encode())
            clientSocket.sendall(date)
        else:
            print("No hay datos de", client_address)
            break
    finally:
        clientSocket.close()
        
