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

def remover_dado(dados_rolados, dados_no_estoque, indice):
    dado = dados_no_estoque[indice]
    dados_rolados.append(dado)
    del dados_no_estoque[indice]

    return [dados_rolados, dados_no_estoque]

def calcula_pontos_regra_simples(lista_int):
    dicio = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for dado in lista_int:
        dicio[dado] += dado
    return dicio

def calcula_pontos_soma (lista):
    soma = 0
    for faces in lista:
        soma += faces
    return soma 

def calcula_pontos_sequencia_baixa (lista_inteiros):
    contador = 1
    pontuacao = 0
    lista_crescente = sorted(set(lista_inteiros))
    i = 1
    while i < len(lista_crescente):
        if lista_crescente[i] - lista_crescente[i-1] == 1:
            contador += 1
            if contador == 4:
                pontuacao = 15
        else: 
            contador = 1
        i += 1
    return pontuacao

def calcula_pontos_sequencia_alta (lista_int):
    contador = 1
    pontuacao = 0
    lista_crescente = sorted(set(lista_inteiros))
    i = 1
    while i < len(lista_crescente):
        if lista_crescente[i] - lista_crescente[i-1] == 1:
            contador += 1
            if contador == 5:
                pontuacao = 30
        else: 
            contador = 1
        i += 1
    return pontuacao