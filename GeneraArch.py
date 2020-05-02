import os

def escrituracsv(log, nombre):
    file = open(nombre + ".csv", "a")
    file. write(log + "\n")
    file. close()