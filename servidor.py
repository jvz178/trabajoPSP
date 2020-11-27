import socket
from threading import Thread
import random

puntuacionTotal=0


class Cliente(Thread):
    def __init__(self, socket_cliente, serv):
        Thread.__init__(self)
        self.socket = socket_cliente
        self.servidor = serv


class Servidor:
    #__init__ es el constructor
    #self se refiere a la instancia actual
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("", 8000))
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
                self.respuestas[pregunta]=listado[1]
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
        if nombre in self.conectados:
            self.conectados.remove(nombre)
            self.usuarioGrupo.pop(nombre)
            return "ok"
        return "logout imposible"

    def listarCompeticiones(self):
        fichero = open("competiciones.txt")
        competiciones = {}
        lista_competiciones = []
        for competicion in range(10):
             listado = []
             listado.append(fichero.readline())
             listado.append(fichero.readline())
             listado.append(fichero.readline())
             lista_competiciones.append(listado)
        competiciones[competicion] = lista_competiciones
        return competiciones

    # Marcar las competiciones (inscritas, finalizadas y en curso)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", 9999))
    server.listen(1)

    def inscribir(self, nombre, participantes):
        if nombre in self.equipos.keys():
            return "imposible inscribir equipo"
        self.equipos[nombre] = participantes
        self.puntuaciones[nombre] = 0
        return "ok"

    def mostrarPreguntas(self, competicion):
        if competicion in self.competiciones.keys():
            return self.competiciones[competicion]
        return "La competicion no esta en curso"

    def recibirRespuesta(self, competicion,  pregunta, respuesta):
        if competicion in self.competiciones.keys():
            if self.respuestas[pregunta]==respuesta:
                self.puntuaciones[pregunta]=1
            self.puntuaciones[pregunta]=-0.2
# Contador, para que cuando llegue a 10 preguntas sumemos las puntuaciones
        for pregunta in range(10):
            puntuacionTotal+=self.puntuaciones[pregunta]
        return puntuacionTotal


servidor1 = Servidor()
