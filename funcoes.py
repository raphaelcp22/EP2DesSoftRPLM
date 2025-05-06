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

def calcula_pontos_sequencia_alta (lista_inteiros):
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

def calcula_pontos_full_house (lista_inteiros):

    contagem_rep = {}

    for dado in lista_inteiros:
        if dado in contagem_rep:
            contagem_rep[dado] += 1
        else:
            contagem_rep[dado] = 1

    ocorrencias = contagem_rep.values()

    if len(contagem_rep) == 2 and 3 in ocorrencias and 2 in ocorrencias:
        valor = 0
        for dado in lista_inteiros:
            valor += dado
        return valor
    else:
        return 0
    
def calcula_pontos_quadra(lista_inteiros):
    contagem_rep = {}

    for dado in lista_inteiros:
        if dado in contagem_rep:
            contagem_rep[dado] += 1
        else:
            contagem_rep[dado] = 1

    for quantidade in contagem_rep.values():
        if quantidade >= 4:
            valor = 0
            for dado in lista_inteiros:
                valor += dado
            return valor

    return 0

def calcula_pontos_quina(lista_inteiros):
    contagem_rep = {}

    for dado in lista_inteiros:
        if dado in contagem_rep:
            contagem_rep[dado] += 1
        else:
            contagem_rep[dado] = 1

    for quantidade in contagem_rep.values():
        if quantidade >= 5:
            valor = 50
            return valor

    return 0

def calcula_pontos_regra_avancada (lista_inteiros):
    return {
    "cinco_iguais": calcula_pontos_quina (lista_inteiros) ,
    "full_house": calcula_pontos_full_house (lista_inteiros) ,
    "quadra": calcula_pontos_quadra(lista_inteiros) ,
    "sem_combinacao" : calcula_pontos_soma(lista_inteiros) ,
    "sequencia_alta" : calcula_pontos_sequencia_alta(lista_inteiros) ,
    "sequencia_baixa" : calcula_pontos_sequencia_baixa(lista_inteiros)
    }


def faz_jogada(dados, categoria, cartela_de_pontos):
    pontuacao_simples = calcula_pontos_regra_simples(dados)
    pontuacao_avancada = calcula_pontos_regra_avancada (dados)
    if categoria not in ["1", "2", "3", "4", "5", "6"]:
        cartela_de_pontos['regra_avancada'][categoria] = pontuacao_avancada[categoria]
    else:
        cat = int(categoria)
        cartela_de_pontos['regra_simples'][cat] = pontuacao_simples [cat]
    return cartela_de_pontos