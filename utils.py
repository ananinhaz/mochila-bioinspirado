import random

def criar_individuo(n):
    return [random.randint(0, 1) for _ in range(n)]

def fitness(individuo, pesos, valores, capacidade):
    peso_total = sum(p * i for p, i in zip(pesos, individuo))
    valor_total = sum(v * i for v, i in zip(valores, individuo))

    # Penaliza a solução se o peso ultrapassar a capacidade
    if peso_total > capacidade:
        return valor_total - (peso_total - capacidade)  # Penaliza o valor com a diferença de peso

    return valor_total

def selecao(populacao, pesos, valores, capacidade, torneio_size=5):
    vencedores = []
    for _ in range(2):  # Seleciona 2 pais
        torneio = random.sample(populacao, torneio_size)
        torneio.sort(key=lambda ind: fitness(ind, pesos, valores, capacidade), reverse=True)
        vencedores.append(torneio[0])  # O vencedor do torneio
    return vencedores

def crossover(pai1, pai2):
    ponto = random.randint(1, len(pai1) - 1)
    return pai1[:ponto] + pai2[ponto:], pai2[:ponto] + pai1[ponto:]

def mutacao(individuo, taxa_mutacao=0.1):
    return [1 - gene if random.random() < taxa_mutacao else gene for gene in individuo]

def elitismo(populacao, pesos, valores, capacidade, elitismo_size=2):
    # Seleciona os melhores 'elitismo_size' indivíduos para manter
    return sorted(populacao, key=lambda ind: fitness(ind, pesos, valores, capacidade), reverse=True)[:elitismo_size]
