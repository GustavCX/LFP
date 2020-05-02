import os

def escrituracsv(log, nombre):
    file = open(nombre + ".csv", "a")
    file. write(log + "\n")
    file. close()

def escrituranorm(log, nombre):
    file = open(nombre + ".dot", "a")
    file. write(log + os.linesep)
    file. close()
