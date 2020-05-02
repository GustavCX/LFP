import os
import Gramatica


opcMenu = 0
opcMenuGramatic = 0
opcReporte = 0 
opcCarga = 0

def caratula():

    print("Lenguajes Formales de Programación")
    print("           Sección A+")
    print("           201700522")
    print("           PROYECTO 2")

    iniciar = input("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    os.system("cls")

salir = False
    
while not salir:

        caratula()
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
                nombreGM = input("\nIngrese el nombre de la gramatica: ")
                if nombreGM:
                    if GT2AP.creaobjGT2(nombreGM):
                        print("Ya existe un afd con el nombre " + nombreGM)
                        try:
                            select = input("¿Desea modificar este AFD? Y/N: ")
                            if select:
                                if select.__eq__("Y") or select.__eq__("y"):
                                    limpiapantalla()
                                    menuGMT2AP(nombreGM)
                        except ValueError:
                            print("El campo está vacío\n")
                    else:
                        limpiapantalla()
                        menuGMT2AP(nombreGM)
                else:
                    print ("Debe ingresar un nombre\n")
                    
            except ValueError:
                print("Error - Debe ingresar un nombre")
           # pausa()       
            
        elif opcMenu == 2:
            os.system("cls")
            menuGramatic()
        #visualizar automata
        elif opcMenu == 3:
            os.system("cls")
            while not opcMnuAFD:
                nameAfdSelect = input("Ingresar el nombre del AFD con el que desea trabajar \n")
                if  not validaAFD(nameAfdSelect):
                    menuEvalCad(nameAfdSelect)
                    break
                else: 
                    print("El nombre del afd no existe")
        #validar cadena     
        elif opcMenu == 4:
            os.system("cls")
            menuCargarArch()
        #Caratula/salir
        elif opcMenu == 5:
            salir = True
            os.system("cls")
            caratula()
        else:
            print("Intrudicir un número entre 1 y 5")

