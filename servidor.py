import socket

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