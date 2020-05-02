from GeneraArch import escrituranorm
from os import system
import time

def mimetodo(di):
    time.sleep(2)
    system (di)
    

def grafo(nombre, estados, transiciones, inicio, aceptacion):
    file = open(nombre + ".dot", "w")
    file.close()
    escrituranorm("digraph d{", nombre)
    escrituranorm("\trankdir = LR", nombre)
    escrituranorm("\tnode [fontname = \"Arial\"];", nombre)
    #count1 = 1
    
    #CREACION DE VERTICES
    log = "\tnodeStart[shape = point, label=\"\"]"
    escrituranorm(log, nombre)
    #shape=doublecircle
    for indx in estados:
        estacp = False
        for acp in aceptacion:
            if acp == indx:
                estacp = True
        if estacp == True:
            log = "\tnode_" + indx + "[shape = doublecircle, label=\"" + indx +"\"];"
        else:
            if(indx == 'q') and (len(estados) == 4):
                log = "\tnode_" + indx + "[shape = circle, label=\"          " + indx +"          \"];"
            else:
                log = "\tnode_" + indx + "[shape = circle, label=\"" + indx +"\"];"
        escrituranorm(log, nombre)
        #count1+=1
    #CREACION DE ARISTAS
    log = "\tnodeStart->node_"+inicio+"[label = \"Inicio\"]"
    escrituranorm(log, nombre)
    for indx in transiciones:
        log = "\tnode_" + indx[0] + "-> node_" + indx[1] + "[label = \"" + indx[2] + "\"];"
        escrituranorm(log, nombre)
    log = "}"
    escrituranorm(log, nombre)
    
    #generacmd("grafo.cmd")
    generagraf(nombre)
    
def generagraf(nombre):
    #dire = input("Ingresa la dirección de destino del grafo: ")
    #if dire:
    #    di = "dot -Tjpg " +  nombre + ".dot -o "+dire +"\\" + nombre + ".jpg"
    #else:
    di = "dot -Tjpg " +  nombre + ".dot -o " + nombre + "-grafo.jpg"
    mimetodo(di)
    
    