from AP import ObjAP

class objGramatic:
    def __init__(self,nombre):
        self.nombre = nombre
        self.noTerminales = []
        self.terminales = []
        self.noTermIni = ""
        self.producciones = [] 
       # self.historial = []
        self.automataPila = ObjAP(nombre)

    #METODO PARA GRAFO
    def generaArbolGrafo(self):
        pass
        #grafo(self.nombre, self.estados, self.transicion, self.estini, self.estacept)
    
    #METODOS ESPECIALIZADOS Y DE VALIDACIÓN
    def validaProduccion(self, prod): #Conjuntos
        for x in self.producciones:
            if x.__eq__(prod):
                return True
        return False
    def validaNoTerminal(self, nt): #---------------------------------
        for x in self.noTerminales:
            if x.__eq__(nt):
                return True
        return False
    def validaTerminal(self, t): #-----------------------------------
        for x in self.terminales:
            if x.__eq__(t):
                return True
        return False
    
    #VALIDACIÓN ESTADO - ALFABETO
    def validaExistencia(self, elemento): #-------------------------------
        for x in self.noTerminales:
            if x.__eq__(elemento):
                return True
        for x in self.terminales:
            if x.__eq__(elemento):
                return True
        return False
    
    #METODOS DE AGREGACIÓN O DEFINICIÓN
    def agregaNT(self, nt):
        self.noTerminales.append(nt)
    def agregaT(self, t):
        self.terminales.append(t)
    def defineNTermInicio(self, ini):
        self.noTermIni = ini
    def agregaProducion(self, prod):
        self.producciones.append(prod)
    def eliminaProduccion(self, prod):
        self.producciones.remove(prod)

    #METODOS DE RETORNO
    def getNombre(self):
        return self.nombre
    def getNoTerminales(self):
        return self.noTerminales
    def getTerminales(self):
        return self.terminales
    def getNTInicial(self):
        return self.noTermIni
    def getProducciones(self):
        return self.producciones
    def getTipo(self):
        return self.tipo
    def getAP (self):
        return self.automataPila


    