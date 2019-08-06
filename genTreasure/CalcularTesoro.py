#coding=utf-8

# CALCULO DE TESORO SEGUN EL MANUAL DE SWORDS AND WIZARDRY
# Codificado por @oscoder87
# 
# RECONOCIMIENTOS
# redactado en castellano a partir de la traducción de
# Javier "cabohicks" García del manual de Swords & Wizardry de Matthew J. Finch
#
# NOTAS:
#
# Denominaciones resumidas
#    La duracion doble y triple de los pergaminos de
#      proteccion se ha indicado con el adjetivo "mayor
#      y superior"
#    "experiencia enana (habilidades especiales)"
#    "experiencia elfica (habilidades especiales)"
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

from random import randint
from math import floor

def dado(nDados, tamDado, extra=0):
    return nDados * randint(1,tamDado) + extra

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
    #
    
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
    return "Poción de " + pc[i] + " de " + str(dado(1,6,6)) + " turnos."

def pergamino():
    def generarPergamino(n):

        def pergaminoProteccion():
            d = dado(1,8)
            lec = {
            1: "demonios",
            2: "ahogo",
            3: "elementales",
            4: "magia",
            5: "metal",
            6: "veneno",
            7: "muertos vivientes",
            8: "licántropos"
            }
            return lec[d] #fin pergaminoProteccion
    
        def pergaminoMaldito():
            d = dado(1,20)
            lec = {
            1: "Ceguera",
            2: "Aversion",
            3: "Confusion",
            4: "Abatimiento",
            5: "Vortice dimensional",
            6: "Alucinaciones",
            7: "Muerte instantánea",
            8: "Levitar",
            9: "Perdida de experiencia",
            10: "Pierde un punto de caracteristica",
            11: "pegamento mágico",
            12: "Obediencia",
            13: "Parálisis",
            14: "Parálisis masiva",
            15: "Disminucion de tamaño",
            16: "Polimorfar",
            17: "Caer dormido",
            18: "Olor",
            19: "Convertir en piedra",
            20: "Estornudos incontrolables"
            }
            return "maldito de " + lec[d] #fin pergaminoMaldito
    
        def generarTipo():
            r = dado(1,2)
            if r == 1: return "de mago "
            else: return "de clerigo "
        #fin generarTipo
        
        r = ""
        if n == 1:
            r = "conjuro de " + generarTipo() + "de niv. 1\n"
        elif n == 2:
            r = "conjuro de " + generarTipo() + "de niv. " + str(dado(1,3))+ "\n"
        elif n == 3:
            for i in range(2):
                r += "conjuro de " + generarTipo() + "de niv. " + str(dado(1,2)) + "\n"
        elif n == 4:
            for i in range(3):
                r += "conjuro de " + generarTipo() + "de niv. 1\n"
        elif n in [5,11,17]:
            r += pergaminoMaldito() + "\n"
        elif n == 6:
            r += "de protección contra " + pergaminoProteccion() + "\n"
        elif n == 7:
            d = dado(1,4)
            for i in range(2):
                r += "conjuro de " + generarTipo() + "de niv. " + str(d) + "\n"
        elif n == 8:
            for i in range(2):
                r += "conjuro de " + generarTipo() + "de niv. " + str(dado(1,6,1)) + "\n"
        elif n == 9:
            t = generarTipo()
            r += "conjuro de " + t + "de niv. "
            if t == "de mago ":
                r += str(dado(1,6,3))
            else:
                r += str(dado(1,6,1))
            r += "\n"
        elif n == 10:
            for i in range(5):
                r += "conjuro de " + generarTipo() + "de niv. " + str(dado(1,3)) + "\n"
        elif n == 12:
             r += "mayor de protección contra " + pergaminoProteccion() + "\n"
        elif n == 13:
            for i in range(5):
                r += "conjuro de " + generarTipo() + "de niv. " + str(dado(1,6)) + "\n"
        elif n == 14:
            for i in range(6):
                r += "conjuro de " + generarTipo() + "de niv. " + str(dado(1,6)) + "\n"
        elif n == 15:
            for i in range(7):
                r += "conjuro de " + generarTipo() + "de niv. " + str(dado(1,3)) + "\n"
        elif n == 16:
            for i in range(8):
                r += "conjuro de " + generarTipo() + "de niv. " + str(dado(1,3)) + "\n"
        elif n == 18:
            r += "superior de protección contra " + pergaminoProteccion() + "\n"
        return r #fin generar pergamino
    
    #1d20 para seleccionar - en realidad solo hay 18 items en la tabla del manual
    return "Pergamino/s: " + generarPergamino( dado(1,18) )

def armamento():
    def maldicion():
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
                return "experiencia enana (habilidades especiales)"
            elif mag == 11:
                return "experiencia elfica (habiliades especiales"
            elif mag == 12:
                return "lanzar confusión 1/dia"
            elif mag == 13:
                return "evita proyectiles 25% (previo a la tirada de impacto"
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
        if ar >= 14:
            intel = dado(1,4)
            if intel == 1:
                e += espadaMagicaUnica()
            return e
            
            
        
    
    def armaduraMagica():
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
        
    #fin etc y armaduraExcepcional
    d = dado(1,18)
    if d == 1:
        d2 = dado(1,2)
        if d2 == 1:
            return "Escudo maldito " + maldicion()
        else:
            return armaduraMagica() + " maldita " + maldicion()
    elif d == 2:
        return proyectiles() + " +1" 
    elif d == 3:
        return "Escudo +1"
    elif d == 4:
        return armaCC() + " +1"
    elif d == 5:
        return armaduraMagica() + " +1"
    elif d == 6:
        return armaCC() + " maldita " + maldicion()
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




# lectura del numero de XP de la mazmorra zona etc
print("|----------------------------------------------------------|")
print("|                                                          |")
print("| CALCULO DE TESORO SEGUN EL MANUAL DE SWORDS AND WIZARDRY |")
print("| Por el metodo de acumulacion de probabilidad             |")
print("|----------------------------------------------------------|")
valid = False 
while (not valid):
    try:
        XP = int( input("Introducir valor de XP de la aventura: ") )
        valid = True
    except (TypeError,ValueError):
        print("introduce un valor entero por favor")
    
# XP = randint(1500,3000)
#XP = 5000
# se multiplica por 1d3+1
oro = XP * dado(1,3,1)
print("Valor en oro de tesoro: %d" % (oro))
# obtener el numero de multiplos de 100, de 1000 y de 5000
n100 = oro // 100
n1000 = oro // 1000
n5000 = oro // 5000

print(n100, n1000, n5000)

# -> tirar probabilidad de intercambio de 100 mo
cambio100 = dado(1,100) <= n100*10
# -> tirar probabilidad de intercambio de 1000 mo
cambio1000 = dado(1,100) <= n1000*10
# -> tirar probabilidad de intercambio de 5000 mo
cambio5000 = dado(1,100) <= n5000*10

print(cambio100, cambio1000, cambio5000)


# COMPROBACION SI ES DESCONTABLE si no es descontable no se descuenta nada y se tiran los intercambios
descontable = False
d = oro
tesoro = "Tesoro compuesto de:\n"
if cambio5000 or cambio1000 or cambio100:
    if cambio5000:
        d -= 5000
        if dado(1,20) == 20:
            tesoro += oMagMayor() + "\n"
            print("oMagMayor")
        else:
            tesoro += joyeriaMayor() + "\n"
            print("joyaMayor")
    if cambio1000:
        d -= 1000
        if dado(1,20) == 20:
            tesoro += oMagMedio() + "\n"
            print("oMagMedio")
        else:
            tesoro += joyeriaMedia() + "\n"
            print("joyaMedia")
    if cambio100:
        d -= 100
        if dado(1,20) == 20:
            tesoro += oMagMenor() + "\n"
            print("oMagMenor")
        else:
            tesoro += joyeriaMenor() + "\n"
            print("joyaMenor")

if d >= 0:
    descontable = True
if descontable: print("descontable")
else: print("no descontable")
if descontable :
    oro = d
print(oro)
# tesoro += "Y monedas por valor de " + str(oro) + "mo."
tesoro += "Monedas: " + monedasRandom(oro)
print(tesoro)
print("\n presiona intro para terminar")
z = input()
