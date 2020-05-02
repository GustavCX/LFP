from GeneraGraph import grafo

class ObjAP():
    
    def __init__(self, nombre):
        self.tipo = "AP"
        self.nombre = nombre
        self.estados = ["i", "p", "q", "f"]
        self.alfabeto = []
        self.simbolosPila = []
        self.transicion = []
        self.estini = "i"
        self.estacept = ["f"]
        self.pila = []
        self.transGrafo = []

    # METODO PARA GRAFO
    def generaGrafo(self):
        self.creaFormatoTransicion()
        # print(self.transGrafo)
        # e = ["i", "p", "          q          ", "f"]
        grafo(self.nombre, self.estados, self.transGrafo, self.estini, self.estacept)

    #Metodos de grafo  (generar lista transicion)
    def creaFormatoTransicion(self):
        self.transGrafo.clear()
        for tr in self.transicion:
            eI = tr[0][0]
            eL = tr[1][0]
            simb = tr[0][1] + "," + tr[0][2]
            init = True
            for comp in tr[1][1]:
                if init:
                    simb = simb + ";" + comp
                    init = False
                else:
                    simb = simb + comp
            t = [eI, eL, simb]
            self.transGrafo.append(t)

# """ [    --------------- 0 ------------------           -------------------- 1 ---------------------
#         ["estadoAct","caracter","descompila"],          ["estadoSig",     ["Elementos", "Compilados"] ]   z, M, N, z
#           ----0----  ----1----   -----2-----             -----0-----      --------------1------------
#                                                                           -----n----- ------n1------ 
#     ]
# """

    def agregaAlfabeto(self, alfa):
        self.alfabeto = alfa
    def agregaSimbolosPila(self, elem, alfa):
        self.simbolosPila.clear()
        self.simbolosPila.extend(elem)
        self.simbolosPila.extend(alfa)
        self.simbolosPila.append("epsilon")
    def agregaTransicion(self, tran):
        self.transicion.append(tran)
    def cleanTransicion(self):
        self.transicion.clear()
    # def agregaHistorial(self, hist):
    #     if self.historial.__len__() == 10:
    #         self.historial.pop(0)
    #         self.historial.append(hist)
    #     else:
    #         self.historial.append(hist)
        
    #METODOS DE RETORNO
    def getEstados(self):
        return self.estados
    def getAlfa(self):
        return self.alfabeto
    def getEstIni(self):
        return self.estini
    def getEstAcep(self):
        return self.estacept
    def getTran(self):
        return self.transicion
    def getTipo(self):
        return self.tipo
    # def getHistorial(self):
    #     return self.historial

    #Metodos de Pila
    def pushPila(self, elemento):
        self.pila.append(elemento)
    def popPila(self):
        self.pila.pop()
    def peekPila(self):
        elem = "Vacío"
        for elem in self.pila:
            pass
        return elem
    def pilaVacia(self):
        if len(self.pila) == 0:
            return True
        else:
            return False
    def getStatusPila(self):
        ep = ""
        if self.pilaVacia():
            ep = "Vacío"
        for p in list(reversed(self.pila)):
            ep = ep + p
        return ep
    def printPila(self):
        print(self.pila)
    def limpiaPila(self):
        self.pila.clear()