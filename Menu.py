import os.path
import GramT2AP
import time

opcMenu = 0
opcMenuGramatic = 0
opcReporte = 0 
opcCarga = 0

salir = False

def validaNum():
    num=0
    try:
     num = int(input("Seleccione una opción: "))
    except ValueError:
     print("--------Error, Ingrese unicamente números-----------")
    return num

def generaAP(nombre):
    GramT2AP.generaAutomata(nombre)

def visualizarAP(nombre):
    GramT2AP.muestraAPgrafo(nombre)
    stp = input("Presione enter para continuar...")


def caratula():
    print("Lenguajes Formales de Programación")
    print("           Sección A+")
    print("           201700522")
    print("           PROYECTO 2")

    iniciar = input("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    os.system("cls")


def menuGMT2AP(nombre):
    os.system ("cls")
    finalizar = False
    opc = 1
    while finalizar == False:

        print(" ----------------- Gramática "+ nombre +" ----------------- ")

        print("\n1. Ingresar Terminales")
        print("2. Ingresar No Terminales")
        print("3. Ingresar Producciones")
        print("4. Borrar Producciones")
        print("5. NT Inicial")
        print("6. Regresar al menú principal")
        try:
            opc = validaNum()
            if opc==1:
                GramT2AP.agregaTerminal(nombre)
            elif opc == 2:
                GramT2AP.agregaNoTerminal(nombre)
            elif opc == 3:
                if(GramT2AP.verificaTNT(nombre)): #Validar si hay terminales o no terminales
                    GramT2AP.agregaProduccionGT2(nombre)
                else:
                    print("No hay terminales o no terminales registrados")
            elif opc == 4:
                if(GramT2AP.verificaPr(nombre)): #Validar si hay producciones
                    GramT2AP.eliminaProduccionGT2(nombre)
                else:
                    print("No hay producciones registradas")
            elif opc == 5:
                GramT2AP.defineNoTerminalInicial(nombre)
            elif opc == 6:
                if GramT2AP.verificaNTini(nombre):
                    finalizar = True
                else:
                    print("Debe definir un no terminal inicial")
            else:
                print("Ingrese un número entre 1 y 6")
                os.system ("cls")
        except ValueError:
            print("Opción inválida")
            os.system ("cls")
    
caratula()
while not salir:
    print("**************************************")
    print("*              Bienvenido            *")
    print("**************************************")
    print("1. Ingresar Gramática/Modificar")
    print("2. Generar Automata")
    print("3. Visualizar Automata")
    print("4. Validar Cadena")
    print("5. Salir \n")

      
    opcMenu = validaNum()
    opcMnu = False

    if opcMenu == 1:
            try:
                os.system ("cls")
                nombreGM = input("\nIngrese el nombre de la gramatica: ")
                if nombreGM:
                    if GramT2AP.creaobjGT2(nombreGM):
                    
                        print("Ya existe una gramatica con el nombre " + nombreGM)
                        try:
                            select = input("¿Desea modificar esta gramatica? Y/N: ")
                            if select:
                                if select.__eq__("Y") or select.__eq__("y"):
                                    os.system ("cls")
                                    menuGMT2AP(nombreGM)
                        except ValueError:
                            print("El campo está vacío\n")
                    else:
                        os.system ("cls")
                        menuGMT2AP(nombreGM)
                else:
                    print ("Debe ingresar un nombre\n")
                    
            except ValueError:
                print("Error - Debe ingresar un nombre")      
            
    elif opcMenu == 2:
            os.system("cls")
            try:
                nombreGM = input("\nIngrese el nombre de la gramatica: ")
                if nombreGM:
                    if GramT2AP.buscanombre(nombreGM):
                        generaAP(nombreGM)
                    else:
                        print("No existe una gramatica con ese nombre")                            
                        stp = input("Presione enter para continuar...")
                else:
                    print ("Debe ingresar un nombre\n")
                    stp = input("Presione enter para continuar...")
            except ValueError:
                    print("Error - Debe ingresar un nombre")
                    stp = input("Presione enter para continuar...")
        
    elif opcMenu == 3:
            os.system("cls")
            try:
                nombreGM = input("\nIngrese el nombre de la gramatica: ")
                if nombreGM:
                    if GramT2AP.buscanombre(nombreGM):
                        visualizarAP(nombreGM)
                    else:
                        print("No hay una gramatica con ese nombre")                            
                        stp = input("Presione enter para continuar...")
                else:
                    print ("Debe ingresar un nombre\n")
                    stp = input("Presione enter para continuar...")
            except ValueError:
                    print("Error - Debe ingresar un nombre")
                    stp = input("Presione enter para continuar...")     
        
    elif opcMenu == 4:
            os.system("cls")
            try:
                nombreGM = input("\nIngrese el nombre de la gramatica: ")
                if nombreGM:
                    if GramT2AP.buscanombre(nombreGM):
                        if GramT2AP.verificaAPojb(nombreGM):
                            GramT2AP.analizacadena(nombreGM)
                        else:
                            print("No se ha generado el autómata de pila para la gramatica solicitada")
                            stp = input("Presione enter para continuar...")
                    else:
                        print("No hay una gramatica con ese nombre")                            
                        stp = input("Presione enter para continuar...")
                else:
                    print ("Debe ingresar un nombre\n")
                    stp = input("Presione enter para continuar...")
            except ValueError:
                    print("Error - Debe ingresar un nombre")
                    stp = input("Presione enter para continuar...")
                
    elif opcMenu == 5:
            salir = True
            os.system("cls")
            caratula()
     
    else:
            print("Intrudicir un número entre 1 y 5")
