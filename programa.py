from funcoes import *

numero_rodadas = 0

tabela_pontos = {
    'pontuacao_simples': {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1
    },
    'pontuacao_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

dados_atuais = rolar_dados(5)
dados_guardados = []

def jogar_rodada(tabela_pontos, dados_atuais, dados_guardados):
    rerrolagens_feitas = 0
    print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
    acao = input('>')
    while acao != '0':
        if acao == '1':
            print('Digite o índice do dado a ser guardado (0 a 4):')
            indice = int(input('>'))
            lista_dados = guardar_dado(dados_atuais, dados_guardados, indice)
            dados_atuais = lista_dados[0]
            dados_guardados = lista_dados[1]
            print(f'Dados rolados: {dados_atuais}')
            print(f'Dados guardados: {dados_guardados}')
        elif acao == '2':
            print('Digite o índice do dado a ser removido (0 a 4):')
            indice = int(input('>'))
            lista_dados = remover_dado(dados_atuais, dados_guardados, indice)
            dados_atuais = lista_dados[0]
            dados_guardados = lista_dados[1]
            print(f'Dados rolados: {dados_atuais}')
            print(f'Dados guardados: {dados_guardados}')
        elif acao == '3':
            if rerrolagens_feitas == 2:
                print('Você já usou todas as rerrolagens.')
            else:
                dados_atuais = rolar_dados(len(dados_atuais))
                rerrolagens_feitas += 1
            print(f'Dados rolados: {dados_atuais}')
            print(f'Dados guardados: {dados_guardados}')
        elif acao == '4':
            imprime_cartela(tabela_pontos)
            print(f'Dados rolados: {dados_atuais}')
            print(f'Dados guardados: {dados_guardados}')
        else:
            print("Opção inválida. Tente novamente.")
        print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
        acao = input('>')

    dados_finais = dados_atuais + dados_guardados
    print('Digite a combinação desejada:')
    escolha_combinacao = input('>')
    opcoes_numericas = ['1', '2', '3', '4', '5', '6']
    while True:
        if escolha_combinacao in opcoes_numericas:
            categoria = int(escolha_combinacao)
        else:
            categoria = escolha_combinacao

        if (categoria in tabela_pontos['pontuacao_simples'] and tabela_pontos['pontuacao_simples'][categoria] != -1) or \
           (categoria in tabela_pontos['pontuacao_avancada'] and tabela_pontos['pontuacao_avancada'][categoria] != -1):
            print("Essa combinação já foi utilizada.")
            escolha_combinacao = input('> ')
        elif categoria not in tabela_pontos['pontuacao_simples'] and categoria not in tabela_pontos['pontuacao_avancada']:
            print("Combinação inválida. Tente novamente.")
            escolha_combinacao = input('> ')
        else:
            break

    faz_jogada(dados_finais, categoria, tabela_pontos)
    return tabela_pontos

contador_rodadas = 0
imprime_cartela(tabela_pontos)
print(f'Dados rolados: {dados_atuais}')
print(f'Dados guardados: {dados_guardados}')

while contador_rodadas < 12:
    tabela_pontos = jogar_rodada(tabela_pontos, dados_atuais, dados_guardados)
    dados_atuais = rolar_dados(5)
    dados_guardados = []
    if contador_rodadas != 11:
        print(f'Dados rolados: {dados_atuais}')
        print(f'Dados guardados: {dados_guardados}')
    contador_rodadas += 1

subtotal_simples = 0
pontuacao_total = 0

for tipo_regra, valores in tabela_pontos.items():
    for pontuacao in valores.values():
        pontuacao_total += pontuacao
        if tipo_regra == 'pontuacao_simples':
            subtotal_simples += pontuacao

if subtotal_simples >= 63:
    pontuacao_total += 35

imprime_cartela(tabela_pontos)
print(f'Pontuação total: {pontuacao_total}')