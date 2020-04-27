import os

listaGramatica =[]

opcMenu = 0
opcMenuAFD = 0
opcMenuGramatic = 0
opcMenuEvalCad = 0
opcReporte = 0 
opcCarga = 0


def validaGram(nombreGram):
    for tmp in listaGramatica:
        if 

def menuEvalCad(AfdSelect):
    
    while  not salirEvalCad:
        print("*************** EVALUAR CADENA CON LA GRAMATICA \"" +AfdSelect+ "\" ***************")
        print("1. Solo validar")
        print("2. Ruta en AFD")
        print("3. Expandir con Gramática")
        print("4. Ayuda")
        print("5. Salir \n")

  
        opcMenuEvalCad = validaNum()
    
        if opcMenuEvalCad == 1:
            cadenita = input("Ingrese la cadena a Evaluar: ")
            EvaluarCadena.EvaluarCad(cadenita,AfdSelect,listaAFD)

        elif opcMenuEvalCad == 2:
            cadenita = input("Ingrese la cadena a Evaluar: ")
            RutaAfd.Ruta(cadenita,AfdSelect,listaAFD)

        elif opcMenuEvalCad == 3:
            cadenita = input("Ingrese la cadena a Evaluar: ")
            ExpandGramatic.Expand(cadenita,AfdSelect,listaAFD)

        elif opcMenuEvalCad == 4:
            ayuda()
        elif opcMenuEvalCad == 5:
            os.system("cls")
            break
        else:
            print("Intrudicir un número entre 1 y 5")

def menuCargarArch():
    while  not salirEvalCad:
        print("*************** CARGAR ARCHIVO ***************")
        print("1. Cargar AFD -> .afd")
        print("2. CArgar Gramática -> .grm")
        print("3. Salir \n")

  
        opcCarga = validaNum()
    
        if opcCarga == 1:
            print("esta es la nueva opcion 1 omega")
            print("")
        elif opcCarga == 2:
            print("esta es la opcion 2")
        elif opcCarga == 3:
            os.system("cls")
            break
        else:
            print("Intrudicir un número entre 1 y 3")

def menuReporte():

    while  not salirReport:
        print("*************** REPORTES ***************")
        print("1. Ver Detalles")
        print("2. Generar Reporte")
        print("3. Ayuda ")
        print("4. Salir\n")

  
        opcReporte = validaNum()
    
        if opcReporte == 1:
            # os.system("cls")
            afdBus = input("Mostrar detalles del AFD: \n")
            detalleAFD(afdBus)
            
        elif opcReporte == 2:
            print("esta es la opcion 2")
        elif opcReporte == 3:
            ayuda()
        elif opcReporte == 4:
            os.system("cls")
            break
        else:
            print("Intrudicir un número entre 1 y 4")

def validaNum():
    num=0
    try:
     num = int(input("Seleccione una opción: "))
    except ValueError:
     print("--------Error, Ingrese unicamente números-----------")
    return num

 # menu inicial...................................
 
salir = False

def caratula():

    print("Lenguajes Formales de Programación")
    print("           Sección A+")
    print("           201700522")
    print("           PROYECTO 2")

    iniciar = input("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    os.system("cls")


    
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
        #ingresar gramatica/editar
        if opcMenu == 1:
            os.system("cls")
            while not opcMnu:
                nuevoAfd  = input("Ingresar el nombre de la gramatica: \n")
                if validaAFD(nuevoAfd):
                    menuAFD(nuevoAfd)
                    break
                else:
                    print("#### El nombre del afd ya existe ####")
        #Generar Automata      
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
            print("Intrudicir un número entre 1 y 6")

caratula()
