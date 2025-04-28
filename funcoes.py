from random import *

def rolar_dados(rodadas):
    lista = []
    i = 0
    for i in range (rodadas) :
        numeros = randint(1,6)
        lista.append(numeros)

    return lista