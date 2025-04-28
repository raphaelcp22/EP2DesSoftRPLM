from random import *

def rolar_dados(rodadas):
    lista = []
    i = 0
    for i in range (rodadas) :
        numeros = randint(1,6)
        lista.append(numeros)

    return lista

def guardar_dado (dados_rolados, dados_no_estoque, indice):
    dados_finais = dados_no_estoque

    valor_guardado = dados_rolados[indice]
    del dados_rolados[indice]
    dados_finais.append(valor_guardado)

    return [dados_rolados, dados_finais]

