from funcoes import *

contador_rodadas = 0

tabela_pontuacoes = {
    'regra_simples': {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1
    },
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

dados_jogados = rolar_dados(5)
dados_selecionados = []

def executar_rodada(tabela_pontuacoes, dados_jogados, dados_selecionados):
    rerrolagens_realizadas = 0
    print('Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:')
    escolha = input('>')
    while escolha != '0':
        if escolha == '1':
            print('Digite o índice do dado a ser guardado (0 a 4):')
            indice_dado = int(input('>'))
            resultado = guardar_dado(dados_jogados, dados_selecionados, indice_dado)
            dados_jogados = resultado[0]
            dados_selecionados = resultado[1]
            print(f'Dados rolados: {dados_jogados}')
            print(f'Dados guardados: {dados_selecionados}')
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            escolha = input('>')
        elif escolha == '2':
            print('Digite o índice do dado a ser removido (0 a 4):')
            indice_dado = int(input('>'))
            resultado = remover_dado(dados_jogados, dados_selecionados, indice_dado)
            dados_jogados = resultado[0]
            dados_selecionados = resultado[1]
            print(f'Dados rolados: {dados_jogados}')
            print(f'Dados guardados: {dados_selecionados}')
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            escolha = input('>')
        elif escolha == '3':
            if rerrolagens_realizadas == 2:
                print('Você já usou todas as rerrolagens.')
            else:
                dados_jogados = rolar_dados(len(dados_jogados))
                rerrolagens_realizadas += 1
            print(f'Dados rolados: {dados_jogados}')
            print(f'Dados guardados: {dados_selecionados}')
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            escolha = input('>')
        elif escolha == '4':
            imprime_cartela(tabela_pontuacoes)
            print(f'Dados rolados: {dados_jogados}')
            print(f'Dados guardados: {dados_selecionados}')
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            escolha = input('>')
        else:
            print("Opção inválida. Tente novamente.")
            escolha = input('>')  

    dados_finalizados = dados_jogados + dados_selecionados
    print('Digite a combinação desejada:')
    escolha_combinacao = input('>')
    opcoes_simples = ['1', '2', '3', '4', '5', '6']
    while True:
        if escolha_combinacao in opcoes_simples:
            categoria = int(escolha_combinacao)
        else:
            categoria = escolha_combinacao

        if (categoria in tabela_pontuacoes['regra_simples'] and tabela_pontuacoes['regra_simples'][categoria] != -1) or \
           (categoria in tabela_pontuacoes['regra_avancada'] and tabela_pontuacoes['regra_avancada'][categoria] != -1):
            print("Essa combinação já foi utilizada.")
            escolha_combinacao = input('> ')
        elif categoria not in tabela_pontuacoes['regra_simples'] and categoria not in tabela_pontuacoes['regra_avancada']:
            print("Combinação inválida. Tente novamente.")
            escolha_combinacao = input('> ')
        else:
            break

    faz_jogada(dados_finalizados, escolha_combinacao, tabela_pontuacoes)
    return tabela_pontuacoes

imprime_cartela(tabela_pontuacoes)
print(f'Dados rolados: {dados_jogados}')
print(f'Dados guardados: {dados_selecionados}')
while contador_rodadas < 12:
    tabela_pontuacoes = executar_rodada(tabela_pontuacoes, dados_jogados, dados_selecionados)
    dados_jogados = rolar_dados(5)
    dados_selecionados = []
    if contador_rodadas != 11:
        print(f'Dados rolados: {dados_jogados}')
        print(f'Dados guardados: {dados_selecionados}')
    contador_rodadas += 1

soma_simples = 0
pontuacao_total = 0
for tipo_regra, valores_pontuacao in tabela_pontuacoes.items():
    for pontos in valores_pontuacao.values():
        pontuacao_total += pontos
        if tipo_regra == 'regra_simples':
            soma_simples += pontos

if soma_simples >= 63:
    pontuacao_total += 35

imprime_cartela(tabela_pontuacoes)
print(f'Pontuação total: {pontuacao_total}')