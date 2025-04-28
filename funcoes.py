from random import *

def rolar_dados(rodadas):
    lista = []
    i = 0
    for i in range (rodadas) :
        numeros = randint(1,6)
        lista.append(numeros)

    return lista

def guardar_dado (lista1, lista2, numero):
    dados_rolados = lista1
    dados_no_estoque = lista2
    indice = numero

    dados_no_estoque.append(dados_rolados[indice])
    
    return [dados_rolados, dados_no_estoque]

