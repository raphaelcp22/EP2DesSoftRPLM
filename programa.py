# arquivo de programa
from funcoes import *
import random

CATEGORIAS = [
    "1", "2", "3", "4", "5", "6",
    "sem_combinacao", "quadra", "full_house",
    "sequencia_baixa", "sequencia_alta", "cinco_iguais"
]

cartela = {categoria: None for categoria in CATEGORIAS}

def mostrar_dados(dados_rolados, dados_guardados):
    print(f"Dados rolados: {dados_rolados}")
    print(f"Dados guardados: {dados_guardados}")

def jogada_valida(combinacao, cartela):
    if combinacao not in cartela:
        print("Combinação inválida. Tente novamente.")
        return False
    elif cartela[combinacao] is not None:
        print("Essa combinação já foi utilizada.")
        return False
    return True

def calcular_pontuacao(combinacao, dados):
    if combinacao in ["1", "2", "3", "4", "5", "6"]:
        return pontuacao_simples(dados, int(combinacao))
    elif combinacao == "sem_combinacao":
        return sum(dados)
    elif combinacao == "quadra":
        return pontuacao_quadra(dados)
    elif combinacao == "full_house":
        return pontuacao_full_house(dados)
    elif combinacao == "sequencia_baixa":
        return pontuacao_sequencia_baixa(dados)
    elif combinacao == "sequencia_alta":
        return pontuacao_sequencia_alta(dados)
    elif combinacao == "cinco_iguais":
        return pontuacao_cinco_iguais(dados)
    return 0


for _ in range(12):
    dados_guardados = []
    dados_rolados = [random.randint(1, 6) for _ in range(5)]
    rerrolagens = 0

    while True:
        mostrar_dados(dados_rolados, dados_guardados)
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        acao = input(">")

        if acao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            try:
                i = int(input(">"))
                if 0 <= i < len(dados_rolados):
                    dados_guardados.append(dados_rolados.pop(i))
                else:
                    print("Índice inválido.")
            except:
                print("Entrada inválida.")

        elif acao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            try:
                i = int(input(">"))
                if 0 <= i < len(dados_guardados):
                    dados_rolados.append(dados_guardados.pop(i))
                else:
                    print("Índice inválido.")
            except:
                print("Entrada inválida.")

        elif acao == "3":
            if rerrolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_rolados = [random.randint(1, 6) for _ in dados_rolados]
                rerrolagens += 1

        elif acao == "4":
            imprime_cartela(cartela)

        elif acao == "0":
            print("Digite a combinação desejada:")
            combinacao = input(">").strip()
            if jogada_valida(combinacao, cartela):
                todos_dados = dados_guardados + dados_rolados
                cartela[combinacao] = calcular_pontuacao(combinacao, todos_dados)
                break
        else:
            print("Opção inválida. Tente novamente.")


simples = ["1", "2", "3", "4", "5", "6"]
pontos_simples = sum(cartela[c] for c in simples if cartela[c] is not None)
bonus = 35 if pontos_simples >= 63 else 0
pontuacao_total = sum(p for p in cartela.values() if p is not None) + bonus


imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao_total}")