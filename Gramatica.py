class Gramartic:
    def __init__(self,nombre):
        self.nombre =nombre
        self.Estado = []
        self.Terminales = []
        self.Nterminale = []
        self.produccion = []
        self.NTinicial = ""
        self.estAcepta = []


    def addTerminal(self,terminal):
        if terminal.islower():
            print("ahuevo")
        else:
            print("solo minusculas puto")