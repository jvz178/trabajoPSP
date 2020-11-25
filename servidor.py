import socket
from threading import Thread
import random



class Cliente(Thread):
    def __init__(self, socket_cliente, serv):
        Thread.__init__(self)
        self.socket = socket_cliente
        self.servidor = serv
 



class Servidor:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("", 9999))
        self.server.listen(1)
        self.conectados = [] #nombres de participantes
        self.equipos = {} #nombre_equipo: lista de participantes
        self.puntuaciones = {}
        self.competiciones = self.cargarPreguntas()
        self.usuarioGrupo ={}
        self.respuestas = {} #por cada equipo un diccionario con  por cada competicion sus respuestas

    def cargarPreguntas(self):
        fichero = open("preguntas.txt")
        competiciones = {}
        linea = fichero.readline()
        while linea != "":
            competicion = linea
            lista_preguntas = []
            for pregunta in range(10):
                listado = []
                listado.append(fichero.readline())
                listado.append(int)(fichero.readline())
                listado.append(fichero.readline())
                listado.append(fichero.readline())
                listado.append(fichero.readline())
                lista_preguntas.append(listado)
            competiciones[competicion] = lista_preguntas
            linea = fichero.readline()
        return competiciones

    def login(self, nombre):
        if nombre in self.conectados:
            return "imposible login"
        self.conectados.append(nombre)
        return "ok"
    
    def logout(self, nombre):
        if nombre in conectados:
            self.conectados.remove(nombre)
            self.usuarioGrupo.pop(nombre)
            return "ok"
        return "logout imposible"

    def listar(self):


    def inscribir(self, nombre, participantes):
        if nombre in self.equipos.keys():
            return "imposible inscriubir equipo"
        self.equipos[nombre] = participantes
        self.puntuaciones[nombre] = 0
        return "ok"

    def mostrarPreguntas(self, competicion):
        if competicion in self.competiciones.keys():



# bucle para atender clientes
while 1:
    # Se espera a un cliente
    socket_cliente, datos_cliente = server.accept()
    # Se escribe su informacion
    print ("conectado "+str(datos_cliente))
    hilo = Cliente(socket_cliente)
    hilo.start()
    