#coding=utf-8

# GENERACION DE TESORO para SWORDS AND WIZARDRY
# Codificado por @oscoder87
# 
# RECONOCIMIENTOS
# redactado en castellano a partir de la traducción de
# Javier "cabohicks" García del manual de Swords & Wizardry de Matthew J. Finch
#
# NOTAS:
#
# NORMAS DE LA CASA: se definen tipos de tesoro distinto para que tengan un
# contenido coherente con su entorno
# Salvo el tipo GRAN TESORO que genera el intercambio de 5000 mo según el manual.
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
    return nDados * randrange(1,tamDado+1) + extra

def monedasRandom(m):
    o = m
    peso = dado(1,50)
    c1 = int(peso/100 * o)
    o = m - c1
    p = c1 * 10
    
    peso = dado(1,10)
    c2 = int(peso/100 * o)
    o -= c2
    c = c2 * 100
    print( str(c) + " monedas de cobre\n" + str(p) + " monedas de plata\n" + str(o) + " monedas de oro.")
    
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
    return "Joya por valor de " + str(v) + "mo"



def oMagMenor():
    j = dado(1,4)
    r = ""
    if j == 1:
        r = pocion()
        
    elif j == 2:
        v = dado(1,6)
        for i in range(v): 
            r += "\n" + pergamino()
    elif j == 3:
        v = dado(1,6)
        for i in range(v): 
            r += "\n" + armamento()
    elif j == 4:
        v = dado(1,20)
        for i in range(v): 
            r += "\n" + oMagRemarcable()
            
    return r

def oMagMedio():
    j = dado(1,4)
    r = ""
    if j == 1:
        for i in range(3):
            r += "\n" + pocion()
        
    elif j == 2:
        v = dado(1,6,6)
        for i in range(v): 
            r += "\n" + pergamino()
    elif j == 3:
        v = dado(1,6,6)
        for i in range(v): 
            r += "\n" + armamento()
    elif j == 4:
        v = dado(1,20,20)
        for i in range(v): 
            r += "\n" + oMagRemarcable()
    return r
    
def oMagMayor():
    j = dado(1,4)
    r = ""
    if j == 1:
        for i in range(6):
            r += "\n" + pocion()
        
    elif j == 2:
        v = dado(1,6,12)
        for i in range(v): 
            r += "\n" + pergamino()
    elif j == 3:
        v = dado(1,6,12)
        for i in range(v): 
            r += "\n" + armamento()
    elif j == 4:
        v = dado(1,20,40)
        for i in range(v): 
            r += "\n" + oMagRemarcable()
    return r
# CLASES

class Pergamino:
    tipo = ""
    nivel = 0
    nombre = ""
    maldito = False
    
    def tipoRandom(self):
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
            1: "Ceguera", 2: "Aversion", 3: "Confusion", 4: "Abatimiento",
            5: "Vortice dimensional", 6: "Alucinaciones", 7: "Muerte instantánea",
            8: "Levitar", 9: "Perdida de experiencia", 10: "Pierde un punto de caracteristica",
            11: "pegamento mágico", 12: "Obediencia", 13: "Parálisis",
            14: "Parálisis masiva", 15: "Disminucion de tamaño",
            16: "Polimorfar", 17: "Caer dormido", 18: "Olor",
            19: "Convertir en piedra", 20: "Estornudos incontrolables"
        }
        return "maldito de " + lec[d] #fin pergaminoMaldito
    
    def seleccionHechizo(self,n, t):
        #
        # abrir el xml
        tree = ET.parse("listahechizos.xml")
        raiz = tree.getroot()
        pa = "./" + t + "/hechizo[@niv='" + str(n) + "']" # leer y filtrar la lista
        elem = raiz.findall(pa)
        lista = ["--"]
        for it in elem:
            lista.append(it)
        # contar y sacar un numero
        return lista[dado(1,len(lista)-1)].text # devolver el resultado
    
    def __init__(self, nivel = 1, tipo = "", maldicion = False):
        if tipo == "":
            self.tipo = tipoRandom()
        else:
            self.tipo = tipo
        self.nivel = nivel
        self.maldicion = maldicion
        if self.maldicion:
            self.nombre = self.maldicionRandom()
        elif self.tipo == "proteccion":
            if self.nivel == 2:
                self.nombre = "mayor"
            elif self.nivel == 3:
                self.nombre = "superior"
            
            self.nombre += " de protección contra " + self.proteccionRandom()
        else:
            if self.tipo == "mago":
                self.nombre = "de magia de " 
            elif self.tipo == "clerigo":
                self.nombre = "de clerigo de "
            self.nombre += self.seleccionHechizo(self.nivel, self.tipo)
    
    def __str__(self):
        if not self.maldito:
            return "Pergamino " + self.nombre + " (niv " + str(self.nivel) + ")"
        else:
            return "Pergamino " + self.nombre
    
    # fin de la CLASE Pergamino
# ----------------------------------------------------
def pocion():
    #1d100 y lectura
    pc = { (1,3) : "Control Animal",
           (4,6): "Clariaudiencia",
           (7,9) : "Clarividencia",
           (10,12) : "Disminución",
           (13,15) : "Controlar Dragones",
           (16,18) : "Volver Etéreo",
           (19,21) : "Resistencia al Fuego",
           (22,24) : "Volar",
           (25,25) : "Brebaje Pegajoso",
           (26,27) : "Forma Gaseosa",
           (28,30) : "Fuerza Gigantesca",
           (31,33) : "Crecimiento",
           (34,36) : "Heroísmo",
           (37,39) : "Invisibilidad",
           (40,42) : "Invulnerabilidad",
           (43,45) : "Levitación",
           (46,48) : "Controlar Plantas",
           (49,55) : "Veneno",
           (56,58) : "Resbalar",
           (59,61) : "Encontrar Tesoro",
           (62,64) : "Controlar Muertos Vivientes",
           (65,75) : "Curación Incrementada",
           (76,00) : "Curación"
    }
    
    r = dado(1,100)
    for i in pc.keys():
        if r in i:
            break
    if pc[i] not in ["Curación", "Curación Incrementada"]:
        return "Poción de " + pc[i] + " de " + str(dado(1,6,6)) + " turnos."
    else: 
        return "Poción de " + pc[i]
# ----------------------------------------------------------------------------------
def tablaPergamino(): # APAGNAR ESTO
    def generarPergamino(n):
            
        r = ""
        if n == 1:
            r = "conjuro de " + tipoPergamino() + "de niv. 1\n"
        elif n == 2:
            r = "conjuro de " + tipoPergamino() + "de niv. " + str(dado(1,3))+ "\n"
        elif n == 3:
            for i in range(2):
                r += "conjuro de " + tipoPergamino() + "de niv. " + str(dado(1,2)) + "\n"
        elif n == 4:
            for i in range(3):
                r += "conjuro de " + tipoPergamino() + "de niv. 1\n"
        elif n in [5,11,17]:
            r += pergaminoMaldito() + "\n"
        elif n == 6:
            r += "de protección contra " + pergaminoProteccion() + "\n"
        elif n == 7:
            d = dado(1,4)
            for i in range(2):
                r += "conjuro de " + tipoPergamino() + "de niv. " + str(d) + "\n"
        elif n == 8:
            for i in range(2):
                r += "conjuro de " + tipoPergamino() + "de niv. " + str(dado(1,6,1)) + "\n"
        elif n == 9:
            t = tipoPergamino()
            r += "conjuro de " + t + "de niv. "
            if t == "de mago ":
                r += str(dado(1,6,3))
            else:
                r += str(dado(1,6,1))
            r += "\n"
        elif n == 10:
            for i in range(5):
                r += "conjuro de " + tipoPergamino() + "de niv. " + str(dado(1,3)) + "\n"
        elif n == 12:
             r += "mayor de protección contra " + pergaminoProteccion() + "\n"
        elif n == 13:
            for i in range(5):
                r += "conjuro de " + tipoPergamino() + "de niv. " + str(dado(1,6)) + "\n"
        elif n == 14:
            for i in range(6):
                r += "conjuro de " + tipoPergamino() + "de niv. " + str(dado(1,6)) + "\n"
        elif n == 15:
            for i in range(7):
                r += "conjuro de " + tipoPergamino() + "de niv. " + str(dado(1,3)) + "\n"
        elif n == 16:
            for i in range(8):
                r += "conjuro de " + tipoPergamino() + "de niv. " + str(dado(1,3)) + "\n"
        elif n == 18:
            r += "superior de protección contra " + pergaminoProteccion() + "\n"
        return r #fin generar pergamino
    
    #1d20 para seleccionar - en realidad solo hay 18 items en la tabla del manual
    return "Pergamino/s: " + generarPergamino( dado(1,18) )
# ---------------------------------------------------------------------------------------------------
#ARMAMENTO

def armadura():
    a = dado(1,4)
    ar =["--","Cota de malla", "Armadura de cuero", "Armadura de placas", "Cota de anillos"]
    return ar[a]

def proyectiles():
    p = dado(1,20)
    if p<=8:
        return str(dado(2,6)) + " flechas"
    elif p<=10:
        return str(dado(1,10)) + " piedras para honda"
    elif p== 1:
        return "jabalina"
    elif p<= 15:
        return str(dado(2,4)) + " dardos"
    elif p<=20:
        return str(dado(2,6)) + " virotes para ballesta"

def armaCC():
    def espadaMagicaUnica():
        mag = dado(1,20)
        if mag == 1:
            return "flamigera (+1d6 daño, luz 30 pies)"
        elif mag == 2:
            return "danzarina (pelea levitando sola 3 asaltos contra el mismo oponente con +1,+2 y +3 se reinicia al indicarle otro oponente)"
        elif mag == 3:
            return "detecta trampas"
        elif mag == 4:
            return "ver invisibles"
        elif mag == 5:
            return "detecta magia"
        elif mag == 6:
            return "clariaudiencia"
        elif mag == 7:
            return "volar"
        elif mag == 8:
            return "levitar"
        elif mag == 9:
            return "1 conjuro de sanacion (1d6) al día"
        elif mag == 10:
            return "confiere habilidades de enano"
        elif mag == 11:
            return "confiere habilidades de elfo"
        elif mag == 12:
            return "lanzar confusión 1/dia"
        elif mag == 13:
            return "evita proyectiles 25% (previo a la tirada de impacto)"
        elif mag == 14:
            return "alerta durante el sueño"
        elif mag == 15:
            return "detecta 1 tipo de monstruo"
        elif mag == 16:
            return "detectar bien y mal 20 pies"
        elif mag == 17:
            intel = dado(3,6)
            return "INT " + str(intel) + " comunicación con el portador, ilusión de cambio facial y altura"
        elif mag == 18:
            intel = dado(3,6)
            return "INT " + str(intel) + " comunicación en radio de 10 pies, detección de obj malditos al 50%"
        elif mag == 19:
            intel = dado(3,6)
            return "INT " + str(intel) + " comunicación con el portador y hablar, atravesar roca (20 pies) 2/dia"
        elif mag == 20:
            intel = dado(3,6)
            return "INT " + str(intel) + " comunicación en radio de 10 pies, inmunidad al drenaje de nivel"
    #fin espadamagicaUnica
    ar = dado(1,20)
    if ar <= 2:
        return "Hacha de batalla"
    elif ar == 3:
        return "Hacha de mano"
    elif ar <= 5:
        return "Daga"
    elif ar == 6:
        return "Martillo de guerra"
    elif ar == 7:
        return "Lanza de caballería"
    elif ar <= 10:
        return "Maza pesada"
    elif ar == 11:
        return "Maza ligera"
    elif ar == 12:
        return "Lanza"
    elif ar == 13:
        return "Bastón"
    elif ar == 14:
        e = "Espada corta "
    elif ar == 15:
        e = "Espada a 2 manos "
    elif ar <= 20:
        e = "Espada larga "
    #ademas las espada
    if ar >= 14:
        intel = dado(1,4)
        if intel == 1:
            e += espadaMagicaUnica()
        return e

def maldicionArmamento():
    mal = dado(1,8)
    if mal <= 2:
        return "-1"
    elif mal in [3,4]:
        return "-2"
    elif mal == 5:
        return "-3"
    elif mal == 6:
        return "atraccion de proyectiles +1"
    elif mal == 7:
        return "hace huir del combate"
    elif mal == 8:
        return "hace lanzarse al combate"
    else: return "otra maldicion."
    
def habilidadesCC():
    h = dado(1,8)
    if h <= 5:
        return "+1 al daño"
    elif h == 6:
        return "luz 10 ft."
    elif h == 7:
        return "luz 30 ft."
    elif h == 8:
        return "+4 al daño contra un tipo de enemigo"
            
def armaExcepcional():
    ae = dado(1,12)
    aes = ["--",
           "Arma contundente +1, destruye muertos vivientes",
           "Arma arrojadiza +1, que vuelve a la mano",
           "Arma +1, ataque extra 1/dia",
           "Arma +1, +2 contra tipo de enemigo",
           "Arma +1, +4 contra tipo de enemigo",
           "Arma +2, +3 contra tipo de enemigo",
           "Arma +4",
           "Arma +5",
           "Arma Flamígera +" +  str(dado(1,4,-1)),
           "Arma Helada +" +  str(dado(1,4,-1)),
           "Arma danzarina" ,
           "Arma inteligente +" + str(dado(1,3)) + " con conjuro 1/dia"
           ]
    return aes[ae]

def armaduraExcepcional():
    aE = dado(1,8)
    aEs = ["--",
        armaduraMagica() + " +4",
        "Escudo +4",
        armaduraMagica() + " +5",
        "Escudo +5",
        "Armadura de Desvío de Flechas",
        "Armadura Demoniaca",
        "Armadura Etérea",
        "Armadura Ardiente"
    ]
    return aEs[aE]

def armamento():
    d = dado(1,18)
    if d == 1:
        d2 = dado(1,2)
        if d2 == 1:
            return "Escudo maldito " + maldicionArmamento()
        else:
            return armaduraMagica() + " maldita " + maldicionArmamento()
    elif d == 2:
        return proyectiles() + " +1" 
    elif d == 3:
        return "Escudo +1"
    elif d == 4:
        return armaCC() + " +1"
    elif d == 5:
        return armaduraMagica() + " +1"
    elif d == 6:
        return armaCC() + " maldita " + maldicionArmamento()
    elif d == 7:
        return proyectiles() + " +2"
    elif d == 8:
        return "Escudo +2"
    elif d in [9,11]:
        return armaCC() + " +2"
    elif d == 10:
        return armaduraMagica() + " +2"
    elif d == 12:
        return armaCC() + " +1 con " + habilidadesCC()
    elif d == 13:
        return proyectiles() + " +3"
    elif d == 14:
        return armaCC() + " +3"
    elif d == 15:
        return "Escudo +3"
    elif d == 16:
        return armaduraMagica() + " +3"
    elif d == 17:
        return armaExcepcional()
    elif d == 18:
        return armaduraExcepcional()
    else:
        return "otro arma o armadura"



def oMagRemarcable():
    ## tipo en 1d60
    return "objetoMagicoRemarcable"


def mostrarMenu():
    print("AQUI VA EL MENU\n")

# lectura del numero de XP de la mazmorra zona etc
print("|-------------------------------------------------------|")
print("|                                                       |")
print("|     GENERACIÓN DE TESORO para SWORDS AND WIZARDRY     |")
print("| Metodo alternativo según el tipo de tesoro deseado    |")
print("|-------------------------------------------------------|")

oro = 0
tamano = "pequeno"
while True:
    opcion = ""    
        
    p = Pergamino(2,"clerigo")
    print(p)
    p = Pergamino(3,"mago",True)
    print(p)
    p = Pergamino(6,"mago",False)
    
    # mostrar menu
    mostrarMenu()
    print("Valor en oro de tesoro: %d Es un tesoro %s" % (oro,tamano))
    opcion = input("Introduce una opcion. q para salir: ")
    
    if opcion == "1": # introducir valor de XP
        try:
            XP = int( input("Introducir valor de XP de la aventura: ") )
            
        except (TypeError,ValueError):
            print("introduce un valor entero por favor")
            XP = 0
        # se multiplica por 1d3+1
        oro = XP * dado(1,3,1)
    elif opcion == "2": # introducir valor en monedas de oro
        try:
            oro = int( input("Introducir valor en Oro del tesoro: ") )
            
        except (TypeError,ValueError):
            print("introduce un valor entero por favor")
            XP = 0
    elif opcion == "3": # generar tesoro tipo Biblioteca
        pass
    elif opcion == "4": # generar tesoro tipo 
        pass
    elif opcion == "5":
        pass
    elif opcion == "6":
        pass
    elif opcion == "7":
        pass
    elif opcion == "q": # SALIR
        print("Adios...")
        print("presiona intro para terminar")
        z = input()
        break
    else:
        print("Introduce una opcion válida")
    
    #Tamano del tesoro seleccionado:
    if oro >= 1500 :
        tamano = "grande"
    elif oro >= 500 :
        tamano = "mediano"
    else:
        tamano = "pequeno"
    
    #END WHILE
