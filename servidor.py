import socket
from threading import Thread, Lock
import random
import os, os.path


class Cliente(Thread):
    def __init__(self, socket_cliente,  email_cliente):
        Thread.__init__(self)
        self.socket = socket_cliente
        self.email = email_cliente
        self.grupo= nombre_grupo
        self.competicion = nombre_competicion
        self.pregunta= 10
        self.respuesta = resp




#Levantar servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", 9999))
server.listen(1)
socket_cliente, datos_cliente = server.accept()
print ("Conectado "+str(datos_cliente))

#Recibir mensaje
mensaje = socket_cliente.recv(1024).decode()

#Cerrar
socket_cliente.close()