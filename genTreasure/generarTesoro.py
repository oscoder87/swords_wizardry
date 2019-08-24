#coding=utf-8

# GENERACION DE TESORO para SWORDS AND WIZARDRY
# Codificado por @oscoder87
# 
# RECONOCIMIENTOS
# redactado en castellano a partir de la traducción de
# Javier "cabohicks" García del manual de Swords & Wizardry de Matthew J. Finch
#
# NOTAS:
# Este documento aun cuando mantiene el contenido de objetos y tablas de S&W
# constituye un conjunto de NORMAS DE LA CASA. Pues altera las opciones y
# algunas proporciones de aleatoriedad del reglamento.
# 
# Si se utiliza el filtro para eliminar varios tipos de pociones, se ponderan
# demasiado las pociones curativa y curativa incrementada.
#
# Se definen tipos de tesoro distinto para que tengan un
# contenido coherente con su entorno.
#
# El más similar es GRAN TESORO que genera el intercambio de 5000 mo según el reglamento.
#
# Denominaciones resumidas
#    - La duracion doble y triple de los pergaminos de
#      proteccion se ha indicado con el adjetivo "mayor
#      y superior"
#    - "confiere habilidades de enano"
#    - "confiere habilidades de elfo"
# 
# Generacion aleatoria de las monedas: NORMA DE LA CASA
#
# LICENCIA:
# consultar el resto de reconocimientos y licencias en https://github.com/oscoder87/swords_wizardry

# El uso de los contenidos de este script ha de realizarse bajo las premisas
# de las licencias origen del material:
#    licencias OGL y
#    Swords & Wizardry Compatibility-Statement License (CSL for the Complete Rules)
# 
# Licencia GNU 3.0

from random import randint, randrange
from math import floor
import xml.etree.ElementTree as ET
     
def dado(nDados, tamDado, extra=0):
    s = extra
    for i in range(nDados):
        s += randrange(1,tamDado+1)
    return s

def monedasRandom(m,limO = 90, limP = 90):
    
    o = int(m * limO/100)
    r = m - o
    p = int(r*10*limP/100)
    r = r*10 - p
    c = int(r*10)
    return str(c) + " monedas de cobre\n" + str(p) + " monedas de plata\n" + str(o) + " monedas de oro."
    
def joyeriaMenor():
    j = dado(1,4)
    if j == 1:    
        v = dado(1,6)
    elif j == 2:
        v = dado(1,100,25)
    elif j == 3:
        v = dado(1,100,75)
    elif j == 4:
        v = dado(1,100) * 10
    return "Joya por valor de " + str(v) + "mo"

def joyeriaMedia():
    j = dado(1,4)
    if j == 1:
        v = dado(1,100)
    elif j == 2:
        v = dado(1,6)* 200
    elif j == 3:
        v = dado(1,6)* 300
    elif j == 4:
        v = dado(1,100) * 100
    return "Joya por valor de " + str(v) + "mo"

def joyeriaMayor():
    j = dado(1,4)
    if j == 1:
        v = dado(1,100) * 10
    elif j == 2:
        v = dado(1,100) * 80
    elif j == 3:
        v = dado(1,100) * 120
    elif j == 4:
        v = dado(1,100) * 200
    return "\nJoya por valor de " + str(v) + " mo"



def oMagMenor():
    j = dado(1,4)
    r = ""
    if j == 1:
        r = pocion() + "\n"
    elif j == 2:
        v = dado(1,6)
        r = tablaPergaminos(v)
    elif j == 3:
        v = dado(1,6)
        r = tablaArmas(v)
    elif j == 4:
        v = dado(1,20)
        r += remarcables(v) + "\n"
            
    return r

def oMagMedio():
    j = dado(1,4)
    r = ""
    if j == 1:
        for i in range(3):
            r += pocion() +"\n"
        
    elif j == 2:
        v = dado(1,6,6)
        r += tablaPergaminos(v)
    elif j == 3:
        v = dado(1,6,6)
        r = tablaArmas(v)
    elif j == 4:
        v = dado(1,20,20)
        r += remarcables(v) + "\n"
    return r
    
def oMagMayor():
    j = dado(1,4)
    r = ""
    if j == 1:
        for i in range(6):
            r += pocion() + "\n"
        
    elif j == 2:
        v = dado(1,6,12)
        r += tablaPergaminos(v)
    elif j == 3:
        v = dado(1,6,12)
        r = tablaArmas(v)
    elif j == 4:
        v = dado(1,20,40)
        r += remarcables(v) + "\n"
    return r

# ------------ CLASE PERGAMINO ------------
class Pergamino:
    tipo = ""
    nivel = 0
    nombre = ""
    maldito = False
    
    def tipoRandom():
        r = dado(1,2)
        if r == 1: return "mago"
        else: return "clerigo"
    
    def proteccionRandom(self):
        d = dado(1,8)
        lec = {
            1: "demonios", 2: "ahogo", 3: "elementales", 4: "magia", 5: "metal",
            6: "veneno", 7: "muertos vivientes", 8: "licántropos"
        }
        return lec[d]
    
    def maldicionRandom(self):
        d = dado(1,20)
        lec = {
            1: "Ceguera 3d6 turnos", 2: "Aversion ver tabla 91", 3: "Confusion", 4: "Abatimiento 1d6 dias",
            5: "Vortice dimensional", 6: "Alucinaciones 3d6 dias", 7: "Muerte instantánea",
            8: "Levitar 1 inch", 9: "Perdida de experiencia 1d10x100 px", 10: "Pierde un punto de caracteristica",
            11: "pegamento mágico", 12: "Obediencia 3d6 turnos", 13: "Parálisis 3d6 turnos",
            14: "Parálisis masiva 20ft. 3d6 turnos", 15: "Disminucion de tamaño 1/2 a la mitad, 1/2 6 inch",
            16: "Polimorfar ver tabla 91", 17: "Caer dormido", 18: "Olor 1d8 dias",
            19: "Convertir en piedra", 20: "Estornudos incontrolables 3d6 turnos"
        }
        return "maldito de " + lec[d] #fin pergaminoMaldito
    
    def seleccionHechizo(self,t, n = 1):
        #
        # abrir el xml
        tree = ET.parse("listasHechizos.xml")
        raiz = tree.getroot()
        pa = "./" + t + "/hechizo[@niv='" + str(n) + "']" # leer y filtrar la lista
        elem = raiz.findall(pa)
        lista = ["--"]
        for it in elem:
            lista.append(it)
        # contar y sacar un numero
        return lista[dado(1,len(lista)-1)].text # devolver el resultado
    
    def __init__(self, nivel = 1 , tipo = "", maldicion = False):
        '''
        permite hacer llamadas
        Pergamino(maldicion = True)
        Pergaminio(nivel)
        Pergamino(nivel, tipo)
        Pergamino(tipo = "")
        '''
        self.nivel = nivel
        self.maldito = maldicion
        self.tipo = tipo
        if self.maldito:
            self.tipo = "maldito"
            self.nombre = self.maldicionRandom()
        
        if not self.maldito and self.tipo == "":
            self.tipo = Pergamino.tipoRandom()
        #
        
        if not self.maldito and self.tipo == "proteccion":
            if self.nivel == 2:
                self.nombre = "mayor"
            elif self.nivel >= 3:
                self.nombre = "superior"
            self.nombre += " de protección contra " + self.proteccionRandom()
        elif self.tipo == "mago":
            self.nombre = "arcano de "
            self.nombre += self.seleccionHechizo(self.tipo,self.nivel)
        elif self.tipo == "clerigo":
            self.nombre = "clerical de "
            self.nombre += self.seleccionHechizo(self.tipo,self.nivel)
        
    
    def __str__(self):
        if not self.maldito:
            return "Pergamino " + self.nombre + " (niv " + str(self.nivel) + ")"
        else:
            return "Pergamino " + self.nombre
    
    # fin de la CLASE Pergamino
# -------- CLASE EQUIPO ------------------------------
class Equipo:
    tipo = ""
    nombre = ""
    nivel = 0
    magico = False
    maldito = False
    unica = False
    efectos = ""
    cantidad = 1
    
    def arma(subtipo = ""):
        arbol = ET.parse("listasArmas.xml")
        raiz = arbol.getroot()
        pa = ".//armas/arma"
        if subtipo != "":
            pa += "/[@" + subtipo + "]"
        l = raiz.findall(pa)
        ar = ["--"]
        for i in l:
            for x in range( int(i.attrib["peso"]) ):
                ar.append(i.text)
        return ar[ dado(1,len(ar) - 1) ]
    
    def armadura(escudo = False): #aleatorio segun S&W
        arbol = ET.parse("listasArmas.xml")
        raiz = arbol.getroot()
        pa = "./armaduras/armadura"
        l = raiz.findall(pa)
        ar = ["--"]
        for i in l:
            for x in range( int(i.attrib["peso"]) ):
                ar.append(i.text)
        
        if escudo:
            ar.append("Escudo")
        a = dado(1,len(ar)-1)
        return ar[a]
    # fin armadura
    
    def eligeProyectil(self):
        p = dado(1,20)
        if p <= 8:
            self.cantidad = dado(2,6)
            self.nombre = "flechas"
        elif p <= 10:
            self.cantidad = dado(1,10)
            self.nombre = "piedras para honda"
        elif p == 1:
            self.nombre = "jabalina"
        elif p<= 15:
            self.cantidad = dado(2,4)
            self.nombre = "dardos"
        elif p<=20:
            self.cantidad = dado(2,6)
            self.nombre = "virotes para ballesta"
    # fin eligeProyectil
    
    def efectoMagicoMenor(self):
        r = ET.parse("listasArmas.xml")
        raiz = r.getroot()
        tips = raiz.findall("./menores/prop")
        tr = ["--"]
        for i in tips:
            for x in range( int(i.attrib["peso"])):
                tr.append(i)
        self.efectos += "\n\t" + tr[dado(1,len(tr)-1)].text
    # fin efectoMagico
    
    def espadaUnica():
        return "ESPADA UNICA"
    # fin espadaUnica
    
    def maldicion(self):
        mal = dado(1,8)
        self.efectos += "\nMALDITA"
        if mal <= 2:
            self.nivel = -1
        elif mal in [3,4]:
            self.nivel = -2
        elif mal == 5:
            self.nivel = -3
        elif mal == 6:
            self.efectos += ": atraccion de proyectiles +1"
        elif mal == 7:
            self.efectos += ": hace huir del combate"
        elif mal == 8:
            self.efectos += ": hace lanzarse al combate"
    # fin maldicion
    
    def __init__(self, tipo, magico, nivel=0, maldicion = False, efecto = False):
        # El tipo y que arma o armadura puede ser
        arbol = ET.parse("listasArmas.xml")
        raiz = arbol.getroot()
        
        self.tipo = tipo
        self.magico = magico
        self.nivel = nivel
        if nivel != 0:
            self.magico = True
        self.maldito = maldicion
        
        if self.tipo == "armas":
            self.nombre = Equipo.arma()
        elif self.tipo == "armadura":
            self.nombre = Equipo.armadura()
        elif self.tipo == "armaduras": #incluye la posibilidad de escudo
            self.nombre = Equipo.armadura(True)
        elif self.tipo == "escudo":
            self.nombre = "Escudo"
            self.tipo = "armaduras"
        elif self.tipo == "proyectil":
            self.eligeProyectil()
        else: # si no se especifica tipo
            t = ["--"]
            t.append(Equipo.arma())
            t.append(Equipo.armadura())
            t.append("Escudo")
            n = dado(1,4)
            if n==4: self.eligeProyectil()
            else:
                self.nombre = t[n]
        #si hay una espada averiguar si es unica
        
        if self.maldito: self.maldicion()
        elif self.nombre in ["Espada corta", "Espada a 2 manos","Espada larga"]:
            unica = dado(1,100) <= 25
            if unica:
                self.magico = True
                tips = raiz.findall("./unicas/espada")
                elegida = tips[dado(1,len(tips)-1)]
                self.efectos += "\n\tUNICA: " + elegida.text
                if elegida.attrib["int"] == "si":
                    self.efectos += " INT: " + str(dado(3,6))
        
        if not self.maldito and self.tipo == "armas" and efecto:
            self.efectoMagicoMenor()
        if self.magico:
            self.efectos += " MAGICO"
        #NO CONTEMPLA LAS EXCEPCIONALES
        #fin INIT
        
    def __str__(self):
        r = ""
        if self.cantidad > 1:
            r += str(self.cantidad)
        r += " " + self.nombre + " "
        
        if self.nivel > 0:
            r += "+" + str(self.nivel) + " "
        elif self.nivel <0:
            r += str(self.nivel) + " "
        r += self.efectos
        return r
    # fin STR
    # FIN class Equipo
# -----------------------------------------------
class OMagico:
    nombre = ""
    def __init__(self, clase = "", poder = ""):
        #se construye el xpath
        if clase != "variados":
            if clase == "varitas":
                self.nombre = "Varita "
            elif clase == "anillos":
                self.nombre = "Anillo de "
            elif clase == "bastones":
                self.nombre = "Bastón de "
        ar = ET.parse("listasObjetos.xml")
        raiz = ar.getroot()
        pa = ".//magicos"
        li = ["--"]
        if clase != "":
            pa += "//" + clase
            if poder != "" :
                pa += "/" + poder
        clase[:-1]
        if pa == "":
            #REVISAR PARA CUALQUIER TIPO
            pa = ".//obj"
            self.nombre = "sale cualquiera"
        else:
            elem = raiz.findall(pa+"/obj")
            for i in elem:
                li.append(i.text)
            
            d = dado(1,len(li)-1)
            if li[d] != "Objeto Maldito":
                self.nombre += li[d]
            else:
                malds = ["--"]
                malds.appendall( raiz.findall(".//maldito") )
                self.nombre += malds[ dado(1,len(malds) - 1)].text
        
    def __str__(self):
        return self.nombre
# ----------------------------------------------------
def pocion(elf = True, en = True):
    #1d100 y lectura
    #lectura XML
    tree = ET.parse("listasObjetos.xml")
    raiz = tree.getroot()
    # xpath
    pa = ".//pocion"
    tots = raiz.findall(pa)
    el = []
    ena = []
    if not elf:
        pa = ".//pocion[@elfica]"
        el = raiz.findall(pa)
    if not en:
        pa = ".//pocion/[@enana]"
        ena = raiz.findall(pa)
    elem = [i for i in tots if ((i not in el) and (i not in ena))]
    pc = ["--"]
    for e in elem:
        for i in range(int(e.attrib["peso"]) ):
            pc.append(e)
    #print(len(pc))
    
    r = dado(1,len(pc)-1)
    if pc[r].text not in ["Curación", "Curación Incrementada"]:
        return "Poción de " + pc[r].text + " de " + str(dado(1,6,6)) + " turnos"
    else: 
        return "Poción de " + pc[r].text

# ---- TABLAS SEGUN S&w ----------------------------------------
def tablaPergaminos(num):
    #
    # Según tablas S&W
    #
    
    r = "Pergaminos:\n"
    for x in range(num):
        n = dado(1,18)
        if n == 1:
            r += "\t- " + str(Pergamino(1)) + "\n"
        elif n == 2:
            r += "\t- " + str(Pergamino( dado(1,3) )) + "\n"
        elif n == 3:
            for i in range(2):
                r += "\t- " + str(Pergamino( dado(1,2) )) + "\n"
        elif n == 4:
            for i in range(3):
                r += "\t- " + str(Pergamino(1)) + "\n"
        elif n in [5,11,17]:
            r += "\t- " + str(Pergamino(maldicion = True)) + "\n"
        elif n == 6:
            r += "\t- " + str(Pergamino(1, "proteccion")) + "\n"
        elif n == 7:
            for i in range(2):
                r += "\t- " + str(Pergamino( dado(1,4) )) + "\n"
        elif n == 8:
            for i in range(2):
                r += "\t- " + str(Pergamino( dado(1,6,1) )) + "\n"
        elif n == 9:
            t = Pergamino.tipoRandom()
            if t == "mago":
                r += "\t- " + str(Pergamino(dado(1,6,3),t))
            else:
                r += "\t- " + str(Pergamino(dado(1,6,1),t))
            r += "\n"
        elif n == 10:
            for i in range(5):
                r += "\t- " + str(Pergamino(dado(1,3))) + "\n"
        elif n == 12:
             r += "\t- " + str(Pergamino(2, "proteccion")) + "\n"
        elif n == 13:
            for i in range(5):
                r += "\t- " + str(Pergamino(dado(1,6))) + "\n"
        elif n == 14:
            for i in range(6):
                r += "\t- " + str(Pergamino(dado(1,6))) + "\n"
        elif n == 15:
            for i in range(7):
                r += "\t- " + str(Pergamino(dado(1,6))) + "\n"
        elif n == 16:
            for i in range(8):
                r += "\t- " + str(Pergamino(dado(1,6))) + "\n"
        elif n == 18:
            r += "\t- " + str(Pergamino(3, "proteccion")) + "\n"
    return r #fin tabla pergaminos
    
# ---------------------------------------------------------------------------------------------------
#ARMAMENTO - CHUSCO, CORREGIR
def armaExcepcional():
    #
    # Según tablas S&W
    #
    
##    r = ""
##    arbol = ET.parse("listasArmas.xml")
##    raiz = arbol.getroot()
    #ae = dado(1,12)
    #l = raiz.findall(".//armaexcepcional/excep")
    
    aes = ["--",
           "+1, destruye muertos vivientes",
           "+1, que vuelve a la mano",
           "+1, ataque extra 1/dia",
           "+1, +2 contra tipo de enemigo",
           "+1, +4 contra tipo de enemigo",
           "+2, +3 contra tipo de enemigo",
           "+4",
           "+5",
           "Flamígera +" +  str(dado(1,4,-1)),
           "Helada +" +  str(dado(1,4,-1)),
           "danzarina" ,
           "inteligente +" + str(dado(1,3)) + " con conjuro 1/dia"
           ]
    ae = dado(1,len(aes)-1)
    
    if ae == 1:
        r = Equipo.arma("contundente")
    elif ae == 2:
        r = Equipo.arma("arrojadiza")
    else:
        r = Equipo.arma()
    r += " " + aes[ae] + "\n   EXCEPCIONAL"
    return r

def armaduraExcepcional():
    #
    # Según tablas S&W
    #
    
##    r = ""
##    arbol = ET.parse("listasArmas.xml")
##    raiz = arbol.getroot()
##    #ae = dado(1,12)
##    l = raiz.findall(".//armaduraexcepcional/excep")
##    li=["--"]
##    for i in l:
##        li.append(i)
##    eleg = li[dado(1,len(li)-1)]
##    
##    e = Equipo( eleg.attrib["tipo"], True, int( eleg.attrib["nivel"] ) )
##    e.efecto = eleg.text
##    e.efecto += "\n EXCEPCIONAL"
##    return str(e)
##    
    aEs = ["--",
        Equipo.armadura()+ " +4",
        "Escudo +4",
        Equipo.armadura() + " +5",
        "Escudo +5",
        "Armadura de Desvío de Flechas",
        "Armadura Demoniaca",
        "Armadura Etérea",
        "Armadura Ardiente"
    ]
    return aEs[dado(1,len(aEs)-1)]

def tablaArmas(num = 1):
    #
    # Según tablas S&W
    #
    
    # Equipo(tipo, magico, nivel=0,maldicion=False,efecto=False)
    r = ""
    for i in range(num):
        d = dado(1,18)
        if d == 1:
            r += str( Equipo("armaduras", False, maldicion=True) ) + "\n"
        elif d == 2:
            r += str( Equipo("proyectil",True, nivel = 1) ) + "\n"
        elif d == 3:
            r +=  str( Equipo("escudo", True, 1 ) ) + "\n"
        elif d == 4:
            r +=  str( Equipo("armas", True, 1) ) + "\n"
        elif d == 5:
            r +=  str( Equipo("armadura", True, 1) ) + "\n"
        elif d == 6:
            r +=  str( Equipo("armas",False,maldicion = True ) ) + "\n"
        elif d == 7:
            r +=  str( Equipo("proyectil",True,2) ) + "\n"
        elif d == 8:
            r +=  str( Equipo("escudo",True,2) ) + "\n"
        elif d in [9,11]:
            r +=  str( Equipo("armas", True, 2) ) + "\n"
        elif d == 10:
            r +=  str( Equipo("armadura", True,2) ) + "\n"
        elif d == 12:
            r +=  str( Equipo("armas",True, 1, efecto=True)) + "\n"
        elif d == 13:
            r +=  str( Equipo("proyectiles",True, 3)) + "\n"
        elif d == 14:
            r +=  str( Equipo("armas",True,3)) + "\n"
        elif d == 15:
            r +=  str( Equipo("escudo",True,3)) + "\n"
        elif d == 16:
            r +=  str( Equipo("armadura",True,3)) + "\n"
        elif d == 17:
            r +=  armaExcepcional() + "\n"
        elif d == 18:
            r +=  armaduraExcepcional() + "\n"
        else:
            #r +=  armaduraExcepcional() + "\n"
            pass
    return r

def remarcables(num):
    #
    # Según tablas S&W
    #
        
    r = "Objetos Magicos remarcables:"
    for i in range(num):
        d = dado(1,60)
        if d <= 3:
            r += "\n\t- " + str(OMagico("varitas","menor"))
        elif d <= 6:
            r += "\n\t- " + str(OMagico("anillos", "menor"))
        elif d <= 24:
            r += "\n\t- " + str(OMagico("variados","menor"))
        elif d <= 27:
            r += "\n\t- " + str(OMagico("varitas", "mayor"))
        elif d <= 30:
            r += "\n\t- " + str(OMagico("anillos","mayor"))
        elif d <= 44:
            r += "\n\t- " + str(OMagico("variados", "medio"))
        elif d == 45:
            r += "\n\t- " + str(OMagico("bastones"))
        else:
            r += "\n\t- " + str(OMagico("variados","mayor"))
    return r

# -----------------------------------------------

def mostrarMenu():
    print(
'''\n-------------- MENU --------------
0. Definir tamaño del tesoro en XP
1. Definir valor del tesoro en mo
         ----
2. Tesoro S & W (según el manual)
         ----
3. Tesoro de armería
4. Tesoro de biblioteca
5. Tesoro de alquimista
6. Tesoro mágico
7. Tesoro de clérigo
         ----
8. Multiples intercambios
c. Tesoro compuesto
         ----
r. Reset
s. Guardar en un archivo
         ----
q. SALIR
''')
# ----- TIPOS DE TESORO -----
PEQLIM = 1000
MEDLIM = 5000 # limites de tamaño segun S&W

def tesoroArmeria(mo):
    t = ""
    # Equipo(tipo, magico, nivel=0,maldicion=False,efecto=False)
    if mo < PEQLIM:
        for i in range(dado(1,6)):
            mal = dado(1,10) == 1
            ni = dado(1,3)
            ef = i%4 == 0
            t += str(Equipo("",bool(i%2),ni,mal,ef)) + "\n"
    elif mo < MEDLIM:
        for i in range(dado(1,6,6)):
            mal = dado(1,10) == 1
            ni = dado(1,3)
            ef = i%4 == 0
            t += str(Equipo("",bool(i%2),ni,mal,ef)) + "\n"
    else:
        for i in range(dado(1,6,12)):
            mal = dado(1,10) == 1
            ni = dado(1,3)
            ef = i%4 == 0
            t += str(Equipo("",bool(i%2),ni,mal,ef)) + "\n"
    return t

def tesoroBiblioteca(mo):
    #Pergamino(nivel = 1 , tipo = "", maldicion = False)
    if mo < PEQLIM:
        return tablaPergaminos( dado(1,6) )
    elif mo < MEDLIM:
        return tablaPergaminos( dado(1,6,6) )
    else:
        return tablaPergaminos( dado(1,6,12) )

def tesoroAlquimista(mo):
    t = ""
    #tablaArmas()
    if mo < PEQLIM:
        t += pocion() + "\n"
    elif mo < MEDLIM:
        for i in range(6):
            t += pocion() + "\n"
        t += str( Pergamino( dado(1,3) )) + "\n"
        t += str( Pergamino( dado(1,3,2) )) + "\n"
    else:
        for i in range(12):
            t += pocion() + "\n"
        t += str( Pergamino( dado(1,3) )) + "\n"
        t += str( Pergamino( dado(1,3,2) )) + "\n"
        t += str( Pergamino( dado(1,3,5) )) + "\n"
    return t

def tesoroMagico(mo):
    #
    # Necesario decidir el tipo de reparto.
    # muchos o pocos pergaminos, algun arma o armadura
    # u otros artefactos
    #
    t = ""
    if mo < PEQLIM:
        t += pocion() + "\n"
        
    elif mo < MEDLIM:
        t += str( Pergamino()) + "\n"
    else:
        for i in range(6):
            pass
    return t + " -- NO IMPLEMENTADO --"

def tesoroClerigo(mo):
    r = ""
    
    objsReligiosos = ["--", "cuenco de cerámica", "caliz",
                      "cetro ritual", "codex de ritos",
                      "pebetero", "estatuilla", "vestimenta ritual",
                      "máscara", "icono", "simbolo sagrado"]
    suministrosClerigo = ["vela", "oz. de incienso", "candil",
                             "carga de aceite", "Vial de agua bendita",
                             "estatuilla", "anfora", "devocionario",
                             "calendario", "tapiz", "oz. de tinta"]
    # Selecciono varios elementos al azar.
    if mo < PEQLIM:
        # pergaminos de protección
        for i in range(dado(1,3)):
            r += str(Pergamino(dado(1,2), "proteccion")) + "\n"
        # pergaminos de clerigo
        for i in range(dado(1,3)):
            r += str(Pergamino(dado(1,3), "clerigo")) + "\n"
        # objetos religiosos variados
        
    elif mo < MEDLIM:
        # pergaminos de protección
        for i in range(dado(1,6,2)):
            r += str(Pergamino(dado(1,3), "proteccion")) + "\n"
        # pergaminos de clerigo
        for i in range(dado(1,6,2)):
            r += str(Pergamino(dado(1,3,2), "clerigo")) + "\n"
        # objetos religiosos variados
        
    else:
        # pergaminos de protección
        for i in range(dado(1,5,5)):
            r += str(Pergamino(dado(1,3), "proteccion")) + "\n"
        # pergaminos de clerigo
        for i in range(dado(1,5,5)):
            r += str(Pergamino(dado(1,5,2), "clerigo")) + "\n"
        # objetos religiosos variados
    # generar cantidad y elegir tipo
    return r

def tesoroCompuesto(mo):
    return "NO IMPLEMENTADO"

def tesoroSnw(mo):
    #
    # Según método S&W
    #
    
    # Tamano del tesoro seleccionado:
    prob100 = 10  * int(mo/100)
    prob1000 = 10 * int(mo/1000)
    prob5000 = 10 * int(mo/5000)

    #print(prob100,prob1000,prob5000)
    
    cambio100 = dado(1,100) <= prob100
    cambio1000 = dado(1,100) <= prob1000
    cambio5000 = dado(1,100) <= prob5000
    
    res = mo
    if cambio100:
        #print("cambio100")
        res -= 100
    if cambio1000:
        #print("cambio1000")
        res -= 1000
    if cambio5000:
        #print("cambio5000")
        res -= 5000
    
    if res <= 0 :
        print("Albricias tesoro enorme,\ncontiene tanto los objetos como el total del dinero.")
        res = mo
    t = ""
    
    if cambio100 and dado(1,20) < 20:
        t += joyeriaMenor() + "\n"
    elif cambio100:
        t += oMagMenor() + "\n"
    
    if cambio1000 and dado(1,20) < 20:
        t += joyeriaMedia() + "\n"
    elif cambio1000:
        t += oMagMedio()  + "\n"
        
    if cambio5000 and dado(1,20) < 20:
        t += joyeriaMayor() + "\n"
    elif cambio5000:
        t += oMagMayor()  + "\n"

    t += monedasRandom(res,98,98)
    return t

def multiCambio(mo):
    #
    # Interpretación del metodo de intercambios encontrada
    # en https://www.d20swsrd.com/
    #
    t = ""
    c1 = 0
    c2 = 0
    c3 = 0
    cambios100 = int(mo/100)
    cambios1000 = int(mo/1000)
    cambios5000 = int(mo/5000)

    for i in range(cambios100):
        if dado(1,10) == 10:
            c1 += 1
            if dado(1,20) == 20:
                t+= oMagMenor() + "\n"
            else:
                t += joyeriaMenor() + "\n"
    for i in range(cambios1000):
        if dado(1,10) == 10:
            c2 += 1
            if dado(1,20) == 20:
                t+= oMagMedio() + "\n"
            else:
                t += joyeriaMedia() + "\n"
    for i in range(cambios5000):
        if dado(1,10) == 10:
            c3 += 1
            if dado(1,20) == 20:
                t+= oMagMayor() + "\n"
            else:
                t += joyeriaMayor() + "\n"
                
    restante = mo - c1*100 - c2*1000 - c3*5000
    
    if restante <= 0:
        t += "Tesoro ENORME\n" + monedasRandom(mo,98,98)
    else:
        t += monedasRandom(restante,98,98)
    
    return t

def ponTamano(mo):
    if mo < PEQLIM:
        return "pequeno"
    elif mo < MEDLIM:
        return "mediano"
    else:
        return "grande"


    
# COMIENZO MAIN
print("|-------------------------------------------------------|")
print("|                                                       |")
print("|     GENERACIÓN DE TESORO para SWORDS AND WIZARDRY     |")
print("| Metodo alternativo según el tipo de tesoro deseado    |")
print("|-------------------------------------------------------|")

# PERGAMINOS OK - algun detalle de descripcion no sale
# POCIONES OK

oro = 0
tesoro = ""
tamano = "pequeno"
while True:
    opcion = ""
    # print(pocion())
    
    #for i in range(15):
    #    p = Equipo("armas",False, efecto=True)
    #    print(p)
    
    # mostrar menu
    mostrarMenu()

    print("Valor en oro de tesoro: %d\nEs un tesoro %s" % (oro,tamano))
    opcion = input("Introduce una opcion. q para salir: ")
    if opcion == "0": # Introducir valor de XP
        try:
            XP = int( input("Introducir valor de XP de la aventura: ") )
            
        except (TypeError,ValueError):
            print("introduce un valor entero por favor")
            XP = 0
        # Se multiplica por 1d3+1
        oro = XP * dado(1,3,1)
        tamano = ponTamano(oro)
        
    elif opcion == "1": # Introducir valor en monedas de oro
        try:
            oro = int( input("Introducir valor en Oro del tesoro: ") )
            tamano = ponTamano(oro)
        except (TypeError,ValueError):
            print("introduce un valor entero por favor")
            XP = 0        
    elif opcion == "2": # Tesoro según S&W
        tesoro += tesoroSnw(oro)
    elif opcion == "3": # generar tesoro tipo armería
        tesoro += tesoroArmeria(oro)
    elif opcion == "4": # Generar tesoro tipo biblioteca
        tesoro += tesoroBiblioteca(oro)
    elif opcion == "5": # Alquimista
        tesoro += tesoroAlquimista(oro)
    elif opcion == "6": # Magico
        tesoro += tesoroMagico(oro)
    elif opcion == "7": # Clerigo
        tesoro += tesoroClerigo(oro)
    elif opcion == "8": # interpretación SRD https://www.d20swsrd.com/
        tesoro += multiCambio(oro)
    elif opcion == "c": # COMPUESTO
        tesoro += tesoroCompuesto(oro)
    elif opcion == "s": # guardar a un fichero de texto
        fname = "Tesoro generado.txt"
        con = 0
        pending = True
        while pending:
            try:
                f = open(fname, 'w')
                f.write(tesoro)
                f.close()
                pending = False
            except (OSError, Exception):                
                fname += " - " + str(con)
                con += 1
        #fin while
    elif opcion == "r": # RESET
        tesoro = ""
    elif opcion == "q": # SALIR
        print("Adios...")
        print("presiona intro para terminar")
        z = input()
        break
    else:
        print("Introduce una opcion válida")
    if tesoro != "":
        print("---\nTESORO GENERADO:\n\n" + tesoro)
    
    #END WHILE
