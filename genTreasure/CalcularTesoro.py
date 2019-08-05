# CALCULO DE TESORO SEGUN EL MANUAL DE SWORDS AND WIZARDRY
# Codificado por @oscoder87
# 
# RECONOCIMIENTOS
# redactado en castellano a partir de la traducción de
# Javier "cabohicks" García del manual de 
# Swords & Wizardry de Matthew J. Finch
#
# NOTAS:
# La duracion doble y triple de los pergaminos de
# proteccion se ha indicado con el adjetivo "mayor
# y superior"
#
# LICENCIA:
# 
# El uso de este codigo ha de realizarse bajo las premisas
# de la licencia origen del material:
#    licencias OGL y
#    Swords & Wizardry Compatibility-Statement License (CSL for the Complete Rules)
# 
from random import randint

def dado(nDados, tamDado, extra=0):
    return nDados * randint(1,tamDado) + extra

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
            r += "\n" + oMagRermarcable()
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
    return "arma\n"
    
def oMagRemarcable():
    return "objetoMagicoRemarcable"




# lectura del numero de XP de la mazmorra zona etc
print("|----------------------------------------------------------|")
print("|                                                          |")
print("| CALCULO DE TESORO SEGUN EL MANUAL DE SWORDS AND WIZARDRY |")
print("| Por el metodo de acumulacion de probabilidad             |")
print("|----------------------------------------------------------|")
# XP = int( input("Introducir valor de XP de la aventura: ") )
# XP = randint(1500,3000)
XP = 5000
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
        if dado(1,20) >= 10:
            tesoro += oMagMayor() + "\n"
            print("oMagMayor")
        else:
            tesoro += joyeriaMayor() + "\n"
            print("joyaMayor")
    if cambio1000:
        d -= 1000
        if dado(1,20) >= 10:
            tesoro += oMagMedio() + "\n"
            print("oMagMedio")
        else:
            tesoro += joyeriaMedia() + "\n"
            print("joyaMedia")
    if cambio100:
        d -= 100
        if dado(1,20) >= 10:
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

tesoro += "Y monedas por valor de " + str(oro) + "mo."
print(tesoro)
