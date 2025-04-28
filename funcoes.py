from random import *

def rolar_dados(n):
    lista = []
    for i in range(len(n)):
        numeros = randint(1,6)
        lista.append(numeros)
    return lista