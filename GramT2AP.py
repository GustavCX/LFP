from Gramatica import objGramartic
from os import system, path
from generalog import escrituracsv

listaGT2 = []

def creaobjGT2(nombre):
    if buscanombre(nombre):
        return True
    else:
        objTemp = objGRA(nombre)
        listaGT2.append(objTemp)
        return False

def buscanombre(nombre):
    for gm in listaGT2:
        if gm.getNombre().__eq__(nombre):
            return True
    return False

def verificaAPojb(nombre):
    for gm in listaGT2:
        if gm.getNombre().__eq__(nombre):
            if gm.getAP().getTran():
                return True
    return False
#BUSQUEDA OBJETO
def dameobjeto(nombre):
    for gm in listaGT2:
        if gm.getNombre().__eq__(nombre):
            return gm

def validaMayMin(caracter):
    carlower = caracter.lower()
    if caracter == carlower:
        return True
    else:
        return False

def validaNumero(caracter):
    try:
        caracter = int(caracter)
        return True
    except:
        return False

def agregaTerminal(nombre): #no mayusculas
    obj_GT2 = dameobjeto(nombre)
    agrega = True
    while agrega == True:
        try:
            terminal = input("Ingrese un terminal: ")
            if terminal:
                if obj_GT2.validaTerminal(terminal) == False: #Valida que no esté en la lista
                    if validaNumero(terminal): #Valida si se esta ingresando un numero
                        obj_GT2.agregaT(terminal)
                    else:
                        if validaMayMin(terminal): #Valida si el terminal es minúscula
                            obj_GT2.agregaT(terminal)
                        else:
                            print("No puede agregarse una mayúscula en los terminales")
                else:
                    print("El terminal " + terminal + " no se puede agregar"
                          +"\nYa existe un terminal idéntico registrado\n")
            else:
                print("Debe ingresar un terminal\n")
                agrega = False
        except ValueError:
            print("Debe ingresar un terminal\n")
            agrega = False

def agregaNoTerminal(nombre): #mayusculas
    obj_GT2 = dameobjeto(nombre)
    agrega = True
    while agrega == True:
        try:
            nterminal = input("Ingrese un no terminal: ")
            if nterminal:
                if obj_GT2.validaNoTerminal(nterminal) == False: #Valida que no esté en la lista
                    if validaNumero(nterminal): #Valida si se esta ingresando un numero
                        # obj_GT2.agregaNT(nterminal)
                        print("No se puede agregar un número a los no terminales")
                    else:
                        if validaMayMin(nterminal): #Valida si el terminal es minúscula
                            print("No puede agregarse en los no terminales")
                        else:
                            obj_GT2.agregaNT(nterminal)
                else:
                    print("El no terminal " + nterminal + " no se puede agregar"
                          +"\nYa existe un terminal idéntico registrado\n")
            else:
                print("Debe ingresar un no terminal\n")
                agrega = False
        except ValueError:
            print("Debe ingresar un no terminal\n")
            agrega = False

def agregaProduccionGT2(nombre):
    obj_GT2 = dameobjeto(nombre)
    agrega = True
    while agrega == True:
        try:
            produccion = input("Ingrese la producción: ") # NT > # # # #
            if produccion:
                if produccion.__contains__(">") and produccion.__contains__(" "):
                    separador = produccion.split(" > ")
                    prod = separador[1].split(" ")
                    prdc = [separador[0], prod]  # [ NT, [T & NT]]
                    if obj_GT2.validaNoTerminal(separador[0]) and validaElementosProd(nombre, prod):
                        obj_GT2.agregaProducion(prdc)
                        # muestra(obj_GT2.getProducciones())
                    else:
                        print("Verifique que la producción ingresada sea correcta\n")
                else:
                    print("Se detectaron errores en el formato ingrese la producción nuevamente\n")
            else:
                print("Debe ingresar una producción\n")
                agrega = False
        except ValueError:
            print("Debe ingresar una producción\n")
            agrega = False

def validaElementosProd(nombre, producciones):
    obj_GT2 = dameobjeto(nombre)
    for elemento in producciones:
        if elemento.__eq__("epsilon"):
            existencia = True
        else:
            existencia = obj_GT2.validaExistencia(elemento)
        if existencia == False:
            print("Se detecto un error en los elementos de la producción")
            return False
    return True

def eliminaProduccionGT2(nombre):
    obj_GT2 = dameobjeto(nombre)
    agrega = True
    while agrega == True:
        try:
            produccion = input("Ingrese la producción a eliminar: ") # NT > # # # #
            if produccion:
                if produccion.__contains__(">") and produccion.__contains__(" "):
                    separador = produccion.split(" > ")
                    prod = separador[1].split(" ")
                    prdc = [separador[0], prod] # [NT, [T & NT]]
                    if obj_GT2.validaProduccion(prdc):
                        obj_GT2.eliminaProduccion(prdc)
                        # muestra(obj_GT2.getProducciones())
                    else:
                        print("Verifique que la producción ingresada sea correcta\n")
                else:
                    print("Se detectaron errores en el formato ingrese la producción nuevamente\n")
            else:
                print("Debe ingresar una producción\n")
                agrega = False
        except ValueError:
            print("Debe ingresar una producción\n")
            agrega = False

def verificaTNT(nombre):
    obj_GT2 = dameobjeto(nombre)
    if obj_GT2.getNoTerminales() or obj_GT2.getTerminales():
        return True
    return False
def verificaPr(nombre):
    obj_GT2 = dameobjeto(nombre)
    if obj_GT2.getProducciones():
        return True
    return False
def verificaNTini(nombre):
    obj_GT2 = dameobjeto(nombre)
    if obj_GT2.getNTInicial().__eq__("None"):
        return False
    else:
        return True

def defineNoTerminalInicial(nombre):
    obj_GT2 = dameobjeto(nombre)
    try:
        nterminal = input("Ingrese el no terminal inicial: ")
        if nterminal:
            if obj_GT2.validaNoTerminal(nterminal) == True:
                obj_GT2.defineNTermInicio(nterminal)
            else:
                print(nterminal + " no es un no terminal o no esta registrado\n")
        else:
            print("Debe ingresar un estado\n")
    except ValueError:
        print("Debe ingresar un simbolo\n")  

def generaAutomata(nombre):
    obj_GT2 = dameobjeto(nombre)
    pilatemp = obj_GT2.getAP()
    pilatemp.agregaAlfabeto(obj_GT2.getTerminales())
    pilatemp.agregaSimbolosPila(obj_GT2.getNoTerminales(), obj_GT2.getTerminales())
    pilatemp.cleanTransicion()
    #TRANSICIONES   ϵ
    pilatemp.agregaTransicion([["i","$","$"], ["p",["#"]]])
    #TIPO 1
    inicio = obj_GT2.getNTInicial()
    pilatemp.agregaTransicion([["p","$","$"], ["q",[inicio]]])  # [[Lista],[estado,Lista]]
    #TIPO2
    trcs = obj_GT2.getProducciones()  # [ NT, [T & NT]]
    for t in trcs:
        pilatemp.agregaTransicion([["q","$",t[0]], ["q",t[1]]])
    #TIPO3
    term = obj_GT2.getTerminales()
    for tr in term:
        pilatemp.agregaTransicion([["q",tr,tr], ["q",["$"]]])
    #FIN
    pilatemp.agregaTransicion([["q","$","#"], ["f",["$"]]])

    # print("Terminales:")
    # print(obj_GT2.getTerminales())
    # print("No Terminales:")
    # print(obj_GT2.getNoTerminales())
    # print("No Terminal Inicial:")
    # print(obj_GT2.getNTInicial())
    # print("Producciones:")
    # muestra(obj_GT2.getProducciones())
    # print("\nTransiciones AP:")
    # muestra(obj_GT2.getAP().getTran())

    pilatemp.generaGrafo()
    stp = input("Enter para continuar...")
""" [
        ["estadoAct","caracter","descompila"], 
        ["estadoSig", 
            ["Elementos", "Compilados"]
        ]
    ]
"""
def muestraAPgrafo(nombre):
    name = nombre + "-grafo.jpg"
    if path.isfile(name):
        di = "start " + name
        system (di)
    else:
        print ("La imagen del autómata no existe o no ha sido generada")

def analizacadena(nombre):
    cadena = input("Ingresa la cadena a analizar: ")
    cadHist = list(reversed(list(cadena)))
    if cadena:
        estadoActual = "i"
        objPila = dameobjeto(nombre).getAP()
        objPila.limpiaPila()
        trn = objPila.getTran()
        cimaPila = objPila.peekPila()
        historial = ["PILA$ ENTRADA$ TRANSICION"]
        esValida = True
        for c in cadena:
            consumeCaracter = False
            while consumeCaracter == False:
                # objPila.printPila()
                consumeCaracter, popP, pushP, pushList, estadoSiguiente, trnHist = buscaestadoSiguiente(trn, estadoActual, c, cimaPila)
                # print(consumeCaracter, "   ", popP, "   ", pushP, "   ", pushList, "   ", estadoSiguiente, "   ", trnHist)
                if estadoSiguiente != "Ninguno":
                    estadoActual = estadoSiguiente
                    uniHist = ""
                    for union in list(reversed(cadHist)):
                        uniHist = uniHist + union
                    pilaHist = objPila.getStatusPila()
                    if pilaHist == None:
                        pilaHist = "Vacío"
                    logHist = pilaHist + "$ " + uniHist + "$ " + trnHist
                    # print(pilaHist + "   " + uniHist + "   " + trnHist)
                    historial.append(logHist)
                    if consumeCaracter:
                        cadHist.pop()
                else:
                    esValida = False
                    break
                
                if popP:
                    objPila.popPila()
                if pushP:
                    for pL in list(reversed(pushList)):
                        objPila.pushPila(pL)

                cimaPila = objPila.peekPila()
            if not esValida:
                break
        if objPila.peekPila() == "#":
            #and (esValida == True):
            logHist = "#$ -$ (q, $, #; f, $)"
            historial.append(logHist)
            generacsv(nombre, historial)
        else:
            print("Cadena Inválida")
    else:
        print("Debe ingresar una cadena para analizar")
    stp = input("Presione enter para continuar...")

def buscaestadoSiguiente(transiciones, estadoAct, caracter, caracterPila):
    catchTrans = "None"
    for t in transiciones: # [[Lista-3],[estado,Lista-n]]   
        if t[0][0] == estadoAct and t[0][1] == "$" and t[0][2] == "$":
            return False, False, True, t[1][1].copy(), t[1][0], dameFormato(t)
        elif t[0][0] == estadoAct and t[0][1] == "$" and t[0][2] == caracterPila:
            if t[1][1][0] == caracter:
                return False, True, True, t[1][1].copy(), t[1][0], dameFormato(t)
            elif t[1][1][0] == "epsilon":
                catchTrans = t
        elif t[0][0] == estadoAct and t[0][1] == caracter and t[0][2] == caracterPila:
            return True, True, False, t[1][1].copy(), t[1][0], dameFormato(t)
    if catchTrans != "None":
        return False, True, False, catchTrans[1][1].copy(), catchTrans[1][0], dameFormato(catchTrans)
    else:
        return False, False, False, ["Ninguno"], "Ninguno", "Ninguno"
#Retorno  ---------- consumeCaracter[T/F], popPila[T/F], pushPila[T/F], pushPila[list], estSiguiente, tranHistorial

def dameFormato(tr):
    simb = "(" + tr[0][0] + ", " +tr[0][1] + ", " + tr[0][2] + "; " + tr[1][0] + ", "
    for comp in tr[1][1]:
        simb = simb + comp
    return simb + ")"
    
def generacsv(nombre, historial):
    file = open(nombre + ".csv", "w")
    file.close()
    for h in historial:
        escrituracsv(h, nombre)
    print("Archivo CSV generado exitosamente\n")

def muestra(lista):
    for e in lista:
        print(e)
