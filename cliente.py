import socket

# Vaya tela


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.socket = socket()
        self.socket.conect("localhost", 9999)
        self.conectado = False
    
    def login(self):
        self.socket.send("login:"+nombre)
        respuesta = self.socket.recv(256)
        if respuesta == "ok":
            self.conectado = True
            print("login con exito")
        else: print(respuesta)

    def logout(self):
        if self.conectado:
            self.socket.send("logout:"+nombre)
            respuesta = self.socket.recv(256)
            if respuesta == "ok":
                self.conectado = True
                print("logout con exito")

    def listar(self):
        if self.conectado:
            self.socket.send("listar:"+nombre)
            tam_datos = (int)(self.socket.recv(256))
            listado = self.socket.recv(tam_datos)
            print(listado)
    
    def inscribirGrupo(self):
        if self.conectado:
            nombre_grupo = input("Escriba el nombre del grupo")
            participante1 = input("nombre del segundo participante")
            participante2= input("Escriba el nombre del tercer participante")
            self.socket.send("inscribir:"+nombre_grupo+":"+self.nombre+":"+participante1+":"+participante2)        
            respuesta = self.socket.recv(256)
            if respuesta == "ok":
                print("grupo registrado con exito")
            else: print("imposible registrar el grupo")

    def mostrarPreguntas(self):
        if self.conectado:
            nombre_competicion = input("escriba el nombre de la competicion")
            self.socket.send("mostrar:"+nombre_competicion)
            tam_datos = (int)(self.socket.recv(256))
            listado = self.socket.recv(tam_datos)
            print(listado)

    def enviarRespuesta(self):
        if self.conectado:
            competicion = input("escribe la competicion de la pregunta")
            pregunta = input("escribe la pregunta que vas a responder")
            respuesta= input("escribe la respuesta")
            self.socket.send("respuesta:"+competicion+":"+pregunta+":"+respuesta)
            tam_datos = (int)(self.socket.recv(256))
            respuesta = self.socket.recv(tam_datos)
            print(respuesta)


    def menu(self):
        opciones = {"1":login, "2":logout, "3":listar, "4":inscribirGrupo, "5":mostrarPreguntas, "6":enviarRespuesta}
        print("==== MENU ====")
        print("\t1. login")
        if(self.conectado):
            print("\t2. logout")
            print("\t3. Listar competiciones")
            print("\t4. inscribir grupo")
            print("\t5. monstrar preguntas")
            print("\t6. enviar respuestas")
        print("\t0. Salir")
        opcion = input("Elije una opción:")
        if opcion == "0": return False
        opciones.get(opcion,menu)()
        return True

nombre = input("escriba su identificador")
cliente = Cliente(nombre)
seguir = True
while seguir:
    seguir = cliente.menu()

'''
#Establecemos la conexion
s=socket.socket()
s.connect('localhost', 8000)

#Enviar

s.send("Hola")

#Cerrar conexion
s.close()'''