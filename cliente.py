import socket

#Establecemos la conexion
s=socket.socket()
s.connect('localhost', 9999)

#Enviar
s.send("Hola")

#Cerrar conexion
s.close()