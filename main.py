from dados_teste import pesos, valores, capacidade
from utils import criar_individuo, fitness, selecao, crossover, mutacao, elitismo
import random
import numpy as np
import time

# GA para resolver o problema da Mochila
def algoritmo_genetico(pesos, valores, capacidade, tamanho_populacao=50, geracoes=100, taxa_mutacao=0.1):
    n = len(pesos)
    populacao = [criar_individuo(n) for _ in range(tamanho_populacao)]

    melhor_individuo = None
    melhor_valor = 0

    for _ in range(geracoes):
        nova_populacao = []

        for _ in range(tamanho_populacao // 2):
            pais = selecao(populacao, pesos, valores, capacidade)
            filho1, filho2 = crossover(pais[0], pais[1])
            filho1 = mutacao(filho1, taxa_mutacao)
            filho2 = mutacao(filho2, taxa_mutacao)
            nova_populacao.extend([filho1, filho2])

        # Adiciona elitismo na população
        populacao = elitismo(populacao, pesos, valores, capacidade, elitismo_size=2)
        populacao.extend(nova_populacao)

        # Avalia o melhor indivíduo da geração
        melhor_da_geracao = max(populacao, key=lambda ind: fitness(ind, pesos, valores, capacidade))
        valor = fitness(melhor_da_geracao, pesos, valores, capacidade)

        if valor > melhor_valor:
            melhor_valor = valor
            melhor_individuo = melhor_da_geracao

    # Calcula o peso total do melhor indivíduo
    peso_total = sum(p * i for p, i in zip(pesos, melhor_individuo)) if melhor_individuo else 0

    return melhor_valor, peso_total, melhor_individuo


# Função para rodar os testes com diferentes tamanhos de entrada
def executar_teste(descricao, pesos, valores, capacidade, **kwargs):
    print(f"\n=== Teste: {descricao} ({len(pesos)} itens) ===")
    inicio = time.time()
    valor, peso, individuo = algoritmo_genetico(pesos, valores, capacidade, **kwargs)
    fim = time.time()
    print("Melhor valor encontrado:", valor)
    print("Peso total:", peso)
    print("Tempo de execução: {:.2f} segundos".format(fim - inicio))


if __name__ == "__main__":
    # Teste pequeno
    executar_teste("Pequeno", pesos, valores, capacidade)

    # Teste médio
    pesos_medios = np.random.randint(1, 20, 1000).tolist()
    valores_medios = np.random.randint(10, 100, 1000).tolist()
    capacidade_media = 2000  # Aumentar a capacidade para 2000
    executar_teste("Médio", pesos_medios, valores_medios, capacidade_media, tamanho_populacao=100, geracoes=200)

    # Teste grande
    pesos_grandes = np.random.randint(1, 20, 10000).tolist()
    valores_grandes = np.random.randint(10, 100, 10000).tolist()
    capacidade_grande = 20000  # Aumentar a capacidade para 20000
    executar_teste("Grande", pesos_grandes, valores_grandes, capacidade_grande, tamanho_populacao=150, geracoes=300)
